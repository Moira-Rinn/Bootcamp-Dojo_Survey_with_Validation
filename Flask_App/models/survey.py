from Flask_App.config.mysql_connection import connectToMySQL


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
        query = "INSERT INTO surveys (first_name, last_name, email, location, progLanguages, satisfaction, willReturn, design, content, services, products, message, created_at, updated_at) VALUES(%(firstname)s, %(lastname)s, %(email)s, %(location)s, %(progLanguages)s, %(satisfaction)s, %(willReturn)s, %(design)s, %(content)s, %(services)s, %(products)s, %(message)s, NOW(), NOW());"
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
