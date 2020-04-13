from src.models import Opinion,User,UserFailedResponse,StateLocal,Article,Complain,Constitution 
from graphene_mongo import MongoengineObjectType
from mongoengine.fields import GenericReferenceField

# Opinion Type 
class TThumbUp(MongoengineObjectType):
    class Meta:
        model = Opinion.ThumbUp
   
class TThumbDown(MongoengineObjectType):
    class Meta:
        model = Opinion.ThumbDown
   
class TMessage(MongoengineObjectType):
    class Meta:
        model = Opinion.Message
     
class TOpinion(MongoengineObjectType):
    class Meta:
        model = Opinion.Opinion
   

# User Type

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

        

# State Local Type

class TLocal(MongoengineObjectType):
    class Meta:
        model = StateLocal.Local



class TState(MongoengineObjectType):
    class Meta:
        model = StateLocal.State


class TStateLocal(MongoengineObjectType):
    class Meta:
        model = StateLocal.StateLocal

# Article Type

class TDetails(MongoengineObjectType):
    class Meta:
        model = Article.Details
              

class TArticle(MongoengineObjectType):
    class Meta:
        model = Article.Article
        

# Complain Type

class TComplain(MongoengineObjectType):
    class Meta:
        model = Complain.Complain
    

# Constitution Types

class TSubSubArticle(MongoengineObjectType):
    class Meta:
        model = Constitution.SubSubArticle
    

class TSubArticle(MongoengineObjectType):
    class Meta:
        model = Constitution.SubArticle
    

class TArticleSection(MongoengineObjectType):
    class Meta:
        model = Constitution.ArticleSection
    

class TSection(MongoengineObjectType):
    class Meta:
        model = Constitution.Section
    


class TConstitution(MongoengineObjectType):
    class Meta:
        model = Constitution.Constitution
    


