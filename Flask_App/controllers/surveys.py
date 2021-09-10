from flask import render_template, redirect, request, session, flash
from Flask_App import app
from Flask_App.models.survey import Survey
from Flask_App import Locations
from Flask_App import Languages


@app.route('/')
def index():
    return render_template('index.html', locations=Locations, languages=Languages)


@app.route('/create/survey', methods=['POST'])
def create_survey():
    data = {
        'first_name': request.form['firstName'],
        'last_name': request.form['lastName'],
        'email': request.form['email'],
        'location': request.form['location'],
        'progLanguage': request.form['progLanguage'],
        'satisfaction': request.form['satisfaction'],
        'willReturn': request.form['willReturn'],
        'design': request.form['design'],
        'content': request.form['content'],
        'services': request.form['services'],
        'products': request.form['products'],
        'message': request.form['message']
    }
    new_survey = Survey.save(data)
    return redirect(f'/submitted/{new_survey}')


@app.route('/submitted/<int:survey_id>')
def submitted(survey_id):
    query = "SELECT * FROM surveys WHERE surveys.id = %(id)s;"
    data = {
        'id': survey_id
    }

    results = Survey.get_all(query, data)

    return render_template("details_page.html", survey=results[0])
