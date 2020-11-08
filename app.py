from flask import Flask, render_template, request, flash
from wtforms import Form, StringField, validators, IntegerField, ValidationError
import subprocess, time

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

def style_check(form, field):
    if field.data > 8:
        raise ValidationError('1-8')
    if field.data < 1:
        raise ValidationError('1-8')

class MyForm(Form):
    style = IntegerField('Style',[style_check])
    bias = IntegerField('Bias')
    text = StringField('Text', validators=[validators.Length(min=1, max=50)])


@app.route('/info', methods=['GET', 'POST'])
def info():
	form = MyForm(request.form)
	if request.method == 'POST' and form.validate():
		s = form.style.data-1
		b = form.bias.data
		t = form.text.data
		substring ='python generate.py --animation --text="{}" --bias={} --style={}'.format(t,b,s)
		subprocess.call(substring, shell = True)
          	
	return render_template('info.html', form=form)



if __name__=="__main__":
	app.run(debug=True)