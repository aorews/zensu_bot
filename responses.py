import random

from database import db_query


class Responses:
    repsponses = dict()

    @classmethod
    def collect(cls):
        data = db_query("select job_type, response_type, phrase from responses")
        for job_type, response_type, text in data:
            cls.responses[job_type] = {response_type: text}

    @classmethod
    def get(cls, job_type, response_type):
        try:
            text = cls.repsponses[job_type][response_type]
            phrases = text.split("\n")
            print(phrases)
            return random.choice(phrases)
        except KeyError:
            return None
    
    @classmethod
    def update(cls, job_type, response_type, text):
        cls.repsponses[job_type] = {response_type: text}