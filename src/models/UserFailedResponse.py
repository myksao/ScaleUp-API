from mongoengine import Document
from mongoengine.fields import StringField


class UserFailedResponse(Document):
    response = StringField()