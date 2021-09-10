from flask import Flask, render_template, request, redirect, session
from locations import Locations

Locations = Locations()

app = Flask(__name__)
app.secret_key = "ItsASecret"


@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] = session['visits'] + 1
    else:
        session['visits'] = 1
    return render_template("index.html", locations=Locations)


# @app.route('/submitted', methods=['POST'])
# def count():
#     return redirect('/')


# @app.route('/clear', methods=['POST'])
# def clear():
#     session.pop('visits')

#     return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)