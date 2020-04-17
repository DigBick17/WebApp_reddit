from flask import render_template,url_for,redirect
from main import app,db
from main.forms import userinput
from main.models import User
import requests


db.create_all()

@app.route('/', methods=['GET','POST'])
def homepage():
	form=userinput()
	if form.validate_on_submit():
		entry1=User(Username1=form.username1.data, Username2=form.username2.data)
		db.session.add(entry1)
		db.session.commit()
		return redirect(url_for('result'))
	return render_template("home.html", Form=form)

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/result', methods=['GET','POST'])
def result():
	obj=User.query.all()
	name1=str(obj[-1].Username1)
	name2=str(obj[-1].Username2)
	compare(name1,name2)
	return render_template("result.html", Name=Name)

def compare(name1,name2):
	global Name
	r1=requests.get('https://www.reddit.com/user/%s.json' % name1,headers = {'User-agent': 'wtf 0.1'})
	r2=requests.get('https://www.reddit.com/user/%s.json' % name2,headers = {'User-agent': 'w 0.1'})
	data1=r1.json()
	data2=r2.json()

	for item in data1["data"]['children']:
		if item["kind"]=="t3":
			ups1=item["data"]['ups']
			break
	for Item in data2["data"]['children']:
		if Item["kind"]=="t3":
			ups2=Item["data"]['ups']
			break

	if ups1>ups2:
		Name=name1
	else:
		Name=name2
