from flask import Flask, render_template, request, json
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
        """
        size = int(request.form.get('size'))
        no_features = int(request.form.get('no_features'))
        no_traits = int(request.form.get('no_traits'))
        for _ in range(3):
        """
    model = Lattice(10, 3, 3)
    model.initialize()
    iters = 1000
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
                    f"Step: {step}. Current cultures: {final_cultures[0]}")
    return render_template("index.html",
                           steps=steps, cultures=data)


if __name__ == '__main__':
    app.run(debug=True)
