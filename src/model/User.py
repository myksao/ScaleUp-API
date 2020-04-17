from mongoengine import Document
from mongoengine.fields import StringField

# main schema
class User(Document):
    meta = {'collection': 'users'}
    imei = StringField()
    name = StringField(min_length= 10, max_length= 15)
    userid = StringField(min_length= 10, max_length= 50)
    password = StringField(min_length= 6, max_length= 1024)
    email = StringField(min_length= 10, max_length= 40)
    state = StringField(required=True)
    placeofresidence = StringField(required=True)
    placeoforigin = StringField(required=True)
    telephone =  StringField(required=True, min_length = 14)
