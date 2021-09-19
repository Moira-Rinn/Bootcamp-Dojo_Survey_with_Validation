from Flask_App.config.mysql_connection import connectToMySQL
from flask import flash
import re


class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.location = data['location']
        self.progLanguages = data['progLanguages']
        self.satisfaction = data['satisfaction']
        self.willReturn = data['willReturn']
        self.design = data['design']
        self.content = data['content']
        self.services = data['services']
        self.products = data['products']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls, query, data=None):
        surveys_from_db = connectToMySQL('Dojo_Survey').query_db(query, data)
        surveys = []
        for s in surveys_from_db:
            surveys.append(cls(s))
        return surveys

    @classmethod
    def save(cls, data=None):
        query = "INSERT INTO surveys (first_name, last_name, email, location, progLanguages, satisfaction, willReturn, design, content, services, products, message, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(location)s, %(progLanguages)s, %(satisfaction)s, %(willReturn)s, %(design)s, %(content)s, %(services)s, %(products)s, %(message)s, NOW(), NOW());"
        survey_id = connectToMySQL('Dojo_Survey').query_db(query, data)
        return survey_id

    @classmethod
    def remove_user(cls, query, data=None):
        survey_id = connectToMySQL('Dojo_Survey').query_db(query, data)
        return survey_id

    @classmethod
    def edit_survey(cls, query, data=None):
        survey_id = connectToMySQL('Dojo_Survey').query_db(query, data)
        return survey_id

    @staticmethod
    def registration_validation(data):
        is_valid = True
        name_regex = re.compile(r'^[a-zA-Z]')
        email_regex = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(data['firstName']) == 0 or not name_regex.match(data['firstName']):
            flash("Please enter a <span>valid first name</span>.")
            is_valid = False
        if len(data['lastName']) == 0 or not name_regex.match(data['lastName']):
            flash("Please enter a <span>valid last name</span>.")
            is_valid = False
        if len(data['email']) == 0 or not email_regex.match(data['email']):
            flash("Please enter a <span>valid email</span>.")
            is_valid = False
        return is_valid
