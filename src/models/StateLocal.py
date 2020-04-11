from mongoengine import Document,EmbeddedDocument
from mongoengine.fields import StringField,IntField,EmbeddedDocumentListField


class Local(EmbeddedDocument):
    name = StringField(required = True)
    id = IntField(required = True)

class State(EmbeddedDocument):
    name = StringField(required = True)
    id = IntField(required = True)
    locals = EmbeddedDocumentListField(Local)


# main schema
class StateLocal(Document):
    meta = {'collection': 'statelocal'}
    state = EmbeddedDocumentListField(State)



