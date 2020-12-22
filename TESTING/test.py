from flask import Flask, render_template, \
    Response, json, request, redirect, url_for
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
    if request.method == 'POST':
        size = int(request.form.get('size'))
        no_features = int(request.form.get('no_features'))
        no_traits = int(request.form.get('no_traits'))
        print(url_for('index', size=size,
                      no_features=no_features, no_traits=no_traits))
        return redirect(url_for('index', size=size,
                                no_features=no_features, no_traits=no_traits))
    return render_template('index.html')


"""
@app.route('/simulation')
def simulation():
    size = request.args.get('size')
    return render_template('simulation.html', size=size)
"""


@app.route('/chart-data')
def chart_data():
    def generate_chart_data():
        model = Lattice(10, 4, 2)
        model.initialize()
        iters = 10000000
        while not model.equilibrium() is True:
            for step in range(iters):
                model.update()
                if (iters - step) % 10000 == 0:
                    final_cultures = (len(model.get_culture_count()),
                                      model.get_culture_count())
                    if model.equilibrium() is True:
                        print("Equilibrium")
                        json_data = json.dumps(
                            {'step': -1000, 'cultures': 0})
                        yield f"data:{json_data}\n\n"
                    else:
                        print(
                         f"Step: {step}. Cultures: {final_cultures[0]}")
                        json_data = json.dumps(
                                    {'step': step,
                                     'cultures': final_cultures[0]})
                        yield f"data:{json_data}\n\n"
    return Response(generate_chart_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)
