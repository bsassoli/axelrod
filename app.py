from flask import Flask, render_template, Response, json, request
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


@app.route('/', methods=["GET", "POST"])
def index():
    max_value = request.form.get("max-value")  # get from form
    no_features = request.form.get('no_features')  # get from form
    no_traits = request.form.get('no_traits')  # get from form
    return render_template('index.html', max_value=max_value,
                           no_features=no_features, no_traits=no_traits)


@app.route('/chart-data')
def chart_data():
    max_value = int(request.args.get("max-value", "0"))  # get from params
    no_features = int(request.args.get("no_features", "0"))  # get from params
    no_traits = int(request.args.get("no_traits", "0"))  # get from params
    model = Lattice(max_value, no_features, no_traits)
    model.initialize()

    def generate_random_data():
        iters = 10000000
        if max_value > 0:
            while True:
                for step in range(iters):
                    model.update()
                    if (iters - step) % 10000 == 0:
                        print(model.size, model.no_features, model.no_traits)
                        if model.equilibrium() is True:
                            print('equilibrium')
                            json_data = json.dumps(
                                {'step': step, 'cultures': 'equilibrium'})
                            yield f"data:{json_data}\n\n"
                        else:
                            json_data = json.dumps({'time': step, 'value': len(
                                model.get_culture_count()),
                                'mutations': model.get_cumulative_mutations()})
                            yield f"data:{json_data}\n\n"

    return Response(generate_random_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
