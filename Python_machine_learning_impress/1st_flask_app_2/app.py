from flask import Flask, render_template, request
from wtform import Form, TextAreaField, validators

app = Flask(__name__)

class HelloForm(Form):
    sayhello = TextAreaField("", [validators.DataRequired()])

@app.route("/", methods=["POST"])
def hello():
    form = HelloForm(request.form)
    return render_template("first_app.html", form=form)

@app.route("/hello", methods=["POST"])
def hello():
    form = HelloForm(request.form)
    if request.method == "POST" and form.validate():
        name = request.form["sayhello"]
        return render_template("hello.html", name=name)
    return render_template("first_app.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
