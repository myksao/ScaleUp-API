#convert image to base64
import base64
# You might also find it useful to create python dictionaries
import json
import os
# decrypt password
from cryptography.fernet import Fernet
from dotenv import load_dotenv

from graphene import ObjectType,Field,Int,String,List,NonNull

# sys helps to check if your folder is in the environment variable
# import sys
# print(sys.path)

# Mongodb schema and Graphene Type Def
from src.models import Opinion,StateLocal,Complain,Article,Constitution,User,types
from mongoengine.queryset.queryset import QuerySet
load_dotenv()
cryptkey = os.getenv('key')

opinion = Opinion.Opinion


#convert binary file from the mongodb to base64
def chatimage(eachimage):
    message_bytes = base64.b64encode(eachimage.encode('ascii'))
    base64_message = message_bytes.decode('ascii')
    return base64_message


class RootQuery(ObjectType):

    bills = Field(List(types.TOpinion), sector = Int(), place = String())
    chat = Field(types.TOpinion, sector = Int(), place = NonNull(String),_id =String())
    user = Field(types.TUser , password= NonNull(String), imei = NonNull(String))
    state = Field(types.TStateLocal)
    stalga= Field(types.TStateLocal, name = NonNull(String))
    articles = Field(List(types.TArticle))
    article = Field(types.TArticle, title = NonNull(String))
    complains = Field(List(types.TComplain))
    complain = Field(types.TComplain, _id = NonNull(String))
    constitutions = Field(List(types.TConstitution))
    constitution = Field(types.TConstitution, id=NonNull(Int))




    @staticmethod
    async def resolve_bills(parent,info,sector, place):
        sectorname = await Opinion.opinions(sector=sector)

        if sector != None:
            
            result =  opinion.objects.get(place=place)
            result.switch_collection('education')
            result.save()
            print(result)
            # checkbill =QuerySet(opinion, getsector._get_collection()).get(place=place)
        
            return result
        else:
            return {'message':'No Sector Sent','status':500}
        
        


    @staticmethod
    async def resolve_chat(parent,info,sector, place, _id):
        sectorname = await Opinion.opinions(sector=sector)

        if len(_id)!=0:
            if sector!=None:
                getsector = opinion().switch_collection(sectorname)
                result = opinion.objects(Q(_id=_id)&Q(place=place))
                eachchat = json.loads(result.to_json())
                for messagechat in eachchat['message']:
                    await map(chatimage, messagechat) 
                return eachchat
            else:
                return {'message':'No Sector Sent','status':500}
        else:
            return {'response': 'No chatid error'}
        #Can't be empty , just trying to avoid nullpointerexpection .....

    @staticmethod
    async def resolve_user(parent,info,password,imei):
        checkimei =  User.User.objects(imei=imei)
        if len(checkimei) != 0:
            cipher_suite = Fernet(cryptkey)
            ciphered_password = cipher_suite.encrypt(password)
            if(ciphered_password == checkimei.password):
                return checkimei
            else:
                message = {'response':'Incorrect Password'}
                return message
        else:
            message = {'response':'Not registered'}
            return message

    @staticmethod
    async def resolve_state(parent,info):
        try:
            getall = StateLocal.StateLocal.objects
            return getall
        except Exception:
            print('Ooops No Data')

    @staticmethod
    async def resolve_stalga(parent,info,name):
        try:
            getall = StateLocal.StateLocal.objects(name=name)
            return getall
        except Exception:
            print('Ooops No Data')
    
    @staticmethod
    async def resolve_articles(parent,info):
        try:
            articlelist = Article.Article.objects
            return articlelist
        except Exception:
            print('Ooops No Data')
    
    @staticmethod
    async def resolve_article(parent,info,title):
        try:
            article = Article.Article.objects(title=title)
            return article
        except Exception:
            print('Ooops No Data')
    
    

    @staticmethod
    async def resolve_complains(parent,info):
        try:
            complainpost =  Complain.Complain.objects
            eachpost = json.loads(complainpost.to_json())
            for post in eachpost:
              await  list(map(chatimage,post['images']))

            return eachpost
        except Exception:
            print('Ooops No Data')
    
    @staticmethod
    async def  resolve_complain(parent,info,_id):
        try:
            getcomplain =  Complain.Complain.objects(_id = Int(_id))
            return getcomplain
        except Exception:
            print('Ooops No Data')
        

    @staticmethod
    async def resolve_constitutions(parent,info):
        try:
            constitutions =  Constitution.Constitution.objects
            return constitutions
        except Exception:
            print('Ooops No Data')
        
    @staticmethod
    async def resolve_constitution(parent,info,id):
        try:
            constitution = Constitution.Constitution.objects(id=id)
            return constitution
        except Exception:
            print('Ooops No Data')
        

   

                


                


