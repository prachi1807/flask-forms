from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "hehehehhe"

# Create a form class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NamerForm()
    # validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template("name.html", name=name, form=form)

if __name__=="__main__":
    app.run(debug=True)





