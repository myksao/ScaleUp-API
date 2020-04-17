from mongoengine import Document,EmbeddedDocument
from mongoengine.fields import StringField,IntField,EmbeddedDocumentListField,EmbeddedDocumentField


class Local(EmbeddedDocument):
    meta={'strict':False}
    name = StringField()
    id = IntField()

class State(EmbeddedDocument):
    meta={'strict':False}
    name = StringField()
    id = IntField()
    locals = EmbeddedDocumentListField(Local)


# main schema
class StateLocal(Document):
    meta = {'collection': 'statelocal','strict':False}
    state = EmbeddedDocumentField(State)



