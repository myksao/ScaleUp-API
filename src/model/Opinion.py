from mongoengine import EmbeddedDocument,Document
from mongoengine.fields import StringField,FileField,EmbeddedDocumentField,EmbeddedDocumentListField,IntField,ListField


class ThumbUp(EmbeddedDocument):
    noofvote = IntField(min_length=0)
    votersid = ListField(StringField())


class ThumbDown(EmbeddedDocument):
    noofvote = IntField(min_length=0)
    votersid = ListField(StringField())

class Message(EmbeddedDocument):
    meta ={'strict':False}
    billid = StringField()
    messageid = IntField()
    text = StringField()
    image = StringField()
    timestamp = StringField()
    user= StringField()


# main schema
class Opinion(Document):
    meta={'strict':False}
    place = StringField()
    bill = StringField()
    thumbsup = EmbeddedDocumentField(ThumbUp)
    thumbsdown = EmbeddedDocumentField(ThumbDown)
    message = EmbeddedDocumentListField(Message)



async def opinions(sector):
    if int(sector) == 0:
        return 'health'
    elif int(sector) == 1:
        return 'housing'
    elif int(sector) == 2:
        return 'education'
    elif int(sector) == 3:
        return 'security'

