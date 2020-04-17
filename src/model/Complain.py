from mongoengine import Document
from mongoengine.fields import StringField,ListField


# main schema
class Complain(Document):
    meta = {'collection': 'complain','strict':False}
    post= StringField(required = True)
    images = ListField(StringField())

