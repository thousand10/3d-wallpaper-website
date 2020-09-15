from flask import render_template, url_for
from website import app
from website.forms import Contact_us

@app.route('/', methods=['GET','POST'])
@app.route('/home')
def home_page():
    return render_template('home.html', title='Homepage')


@app.route('/contact', methods=['GET','POST'])
def contact():
    form = Contact_us()
    return render_template('contact.html', title='Contact', form=form)



@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html', title='About')