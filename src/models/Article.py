from mongoengine import Document,EmbeddedDocument
from mongoengine.fields import StringField,EmbeddedDocumentListField



class Details(EmbeddedDocument):
    meta = {'allow_inheritance':True}
    one = StringField()
    two = StringField()
    three = StringField()
    four = StringField()


# main schema
class Article(Document):
    meta = {'collection': 'articles'}
    title = StringField(required = True)
    details = EmbeddedDocumentListField(Details)



