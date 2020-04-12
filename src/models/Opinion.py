from mongoengine import EmbeddedDocument,Document
from mongoengine.fields import StringField,FileField,EmbeddedDocumentField,EmbeddedDocumentListField,IntField,ListField


class ThumbUp(EmbeddedDocument):
    noofvote = IntField(min_length=0)
    votersid = ListField(StringField())


class ThumbDown(EmbeddedDocument):
    noofvote = IntField(min_length=0)
    votersid = ListField(StringField())

class Message(EmbeddedDocument):
    _id: StringField()
    billid: StringField()
    id: IntField()
    text: StringField()
    image: FileField()
    timestamp: StringField()
    user: StringField()


# main schema
class Opinion(Document):
    meta={'collection':'health','strict':False}
    _id = StringField()
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

