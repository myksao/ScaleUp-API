from src.models import Opinion,User,UserFailedResponse,StateLocal,Article,Complain,Constitution 
from graphene_mongo import MongoengineObjectType
from mongoengine.fields import GenericReferenceField


class TOpinion(MongoengineObjectType):
    class Meta:
        model = Opinion.Opinion
   


class TUser(MongoengineObjectType):
    class Meta:
        model = User.User
    response = GenericReferenceField(choices=[User.User, UserFailedResponse.UserFailedResponse])


class TUserFailedResponse(MongoengineObjectType):
    class Meta:
        model = UserFailedResponse.UserFailedResponse


# class TUserResult(Union):
#     class Meta:
#         types = (User.User, UserFailedResponse.UserFailedResponse)

        



class TStateLocal(MongoengineObjectType):
    class Meta:
        model = StateLocal.StateLocal
    


class TArticle(MongoengineObjectType):
    class Meta:
        model = Article.Article
        



class TComplain(MongoengineObjectType):
    class Meta:
        model = Complain.Complain
    


class TConstitution(MongoengineObjectType):
    class Meta:
        model = Constitution.Constitution
    


