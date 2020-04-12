from mongoengine import Document,EmbeddedDocument
from mongoengine.fields import StringField,IntField,EmbeddedDocumentListField


class Local(EmbeddedDocument):
    meta = {'allow_inheritance':True}
    name = StringField(required = True)
    id = IntField(required = True)

class State(EmbeddedDocument):
    meta = {'allow_inheritance':True}
    name = StringField(required = True)
    id = IntField(required = True)
    locals = EmbeddedDocumentListField(Local)


# main schema
class StateLocal(Document):
    meta = {'collection': 'statelocal'}
    state = EmbeddedDocumentListField(State)



