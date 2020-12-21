from flask import Flask, render_template, Response, json
from axelrod import Lattice
# Configure application
app = Flask(__name__)
# Ensure templates are auto-reloaded
# app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/chart-data')
def chart_data():
    def generate_chart_data():
        while True:
            model = Lattice(40, 4, 12)
            model.initialize()
            iters = 100000
            steps = []
            data = []
            for step in range(iters):
                model.update()
                if (iters - step) % 10000 == 0:
                    final_cultures = (len(model.get_culture_count()),
                                      model.get_culture_count())
                    steps.append(step)
                    data.append(final_cultures[0])
                    if model.equilibrium() is True:
                        print("Equilibrium")
                        break
                    else:
                        print(
                            f"Step: {step}. Current cultures: {data}")
                    json_data = json.dumps(
                        {'time': step, 'value': final_cultures[0]})
                    yield f"data:{json_data}\n\n"
    return Response(generate_chart_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)
