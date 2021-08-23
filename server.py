from flask import Flask, render_template, request, redirect, session
from locations import Locations


app = Flask(__name__)
app.secret_key = 'WouldntYouLikeToKnow'

Locations = Locations()


@app.route('/')
def index():
    return render_template('index.html', locations=Locations)


@app.route('/process', methods=['POST'])
def sesData():
    session['firstName'] = request.form['firstName']
    session['lastName'] = request.form['lastName']
    session['email'] = request.form['email']
    session['location'] = request.form['location']
    session['progLanguage'] = request.form['progLanguage']
    session['satisfaction'] = request.form['satisfaction']
    session['willReturn'] = request.form['willReturn']
    session['goodThings'] = request.form.getlist('goodThings')
    session['message'] = request.form['message']

    return redirect('/submitted')


@app.route('/submitted')
def submitted():
    return render_template('submitted.html')


if __name__ == "__main__":
    app.run(debug=True)
