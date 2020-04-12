from mongoengine import Document,EmbeddedDocument
from mongoengine.fields import StringField,IntField,EmbeddedDocumentListField

class SubSubArticle(EmbeddedDocument):
    meta = {'allow_inheritance':True}
    i = StringField()

class SubArticle(EmbeddedDocument):
    meta = {'allow_inheritance':True}
    a = StringField()
    sub = EmbeddedDocumentListField(SubSubArticle)

class ArticleSection(EmbeddedDocument):
    meta = {'allow_inheritance':True}
    one = StringField()
    sub = EmbeddedDocumentListField(SubArticle)

class Section(EmbeddedDocument):
    meta = {'allow_inheritance':True}
    id = IntField(required=True)
    article = EmbeddedDocumentListField(ArticleSection)


# main schema
class Constitution(Document):
    meta = {'collection': 'constitutions'}
    chapter = IntField(required=True)
    title = StringField(required=True)
    section = EmbeddedDocumentListField(Section)



