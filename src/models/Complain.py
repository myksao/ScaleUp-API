from mongoengine import Document
from mongoengine.fields import StringField,FileField,ListField


# main schema
class Complain(Document):
    meta = {'collection': 'complains'}
    post: StringField(required = True)
    images: ListField(FileField())


