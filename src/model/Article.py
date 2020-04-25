from mongoengine import Document,EmbeddedDocument
from mongoengine.fields import StringField,EmbeddedDocumentListField


class One(EmbeddedDocument):
    one = StringField()
    # two = StringField()
    # three = StringField()
    # four = StringField()


# main schema
class Article(Document):
    meta = {'collection': 'article'}
    title = StringField(required = True)
    details = EmbeddedDocumentListField(One)



