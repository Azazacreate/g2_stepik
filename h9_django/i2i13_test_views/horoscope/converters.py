from datetime import datetime
from django.urls import register_converter

class Converter_date:
    regex = '(((0[1-9])|([12][0-9])|(3[01]))-((0[0-9])|(1[012]))-((20[012]\d|19\d\d)|(1\d|2[0123])))'
    def to_python(self, value):
        return datetime.strptime(value, '%d-%m-%Y')
    def to_url(self, value):
        return datetime.strftime(value, '%d-%m-%Y')
