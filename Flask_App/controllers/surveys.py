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
        'progLanguages': request.form['progLanguages'],
        'satisfaction': request.form['satisfaction'],
        'willReturn': int(request.form['willReturn']),
        'design': " ",
        'content': " ",
        'services': " ",
        'products': " ",
        'message': request.form['message']
    }

    if 'design' in request.form:
        data['design'] = request.form['design']
    if 'content' in request.form:
        data['content'] = request.form['content']
    if 'services' in request.form:
        data['services'] = request.form['services']
    if 'products' in request.form:
        data['products'] = request.form['products']

    if not Survey.registration_validation(request.form):
        return redirect('/')
    new_survey = Survey.save(data)
    session['Survey_name'] = request.form['firstName']

    return redirect(f'/submitted/{new_survey}')


@app.route('/submitted/<int:survey_id>')
def submitted(survey_id):
    query = "SELECT * FROM surveys WHERE surveys.id = %(id)s;"
    data = {
        'id': survey_id
    }

    results = Survey.get_all(query, data)

    return render_template("submitted.html", new_survey=results[0])
