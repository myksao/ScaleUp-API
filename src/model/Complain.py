from mongoengine import Document
from mongoengine.fields import StringField,ObjectIdField,ListField


# main schema
class Complain(Document):
    meta = {'collection': 'complain','strict':False}
    _id = ObjectIdField()
    post= StringField(required = True)
    images = ListField(StringField())


