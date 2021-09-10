from flask import Flask, render_template, request, redirect, session
from Flask_App.models.locations import Locations
from Flask_App.models.language import Languages


app = Flask(__name__)
app.secret_key = 'WouldntYouLikeToKnow'

Locations = Locations()
Languages = Languages()
