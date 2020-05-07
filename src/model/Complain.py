from mongoengine import Document,EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentListField,StringField,ObjectIdField,ListField


class Data(EmbeddedDocument):
    data = StringField()

# main schema
class Complain(Document):
    meta = {'collection': 'complain','strict':False}
    _id = ObjectIdField()
    post= StringField(required = True)
    file = EmbeddedDocumentListField(Data)
    fileextension = StringField()


