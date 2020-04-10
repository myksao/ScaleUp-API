from mongoengine import Document,EmbeddedDocument
from mongoengine.fields import StringField,IntField,EmbeddedDocumentListField,ReferenceField

class SubSubArticle(EmbeddedDocument):
    i = StringField()

class SubArticle(EmbeddedDocument):
    a = StringField()
    sub = EmbeddedDocumentListField(SubSubArticle)

class ArticleSection(EmbeddedDocument):
    one = StringField()
    sub = EmbeddedDocumentListField(SubArticle)

class Section(EmbeddedDocument):
    id = IntField(required = True)
    article = EmbeddedDocumentListField(ArticleSection)


# main schema
class Constitution(Document):
    meta = {'collection': 'constitutions'}
    chapter = IntField(required = True)
    title = StringField(required = True)
    section = EmbeddedDocumentListField(Section)



