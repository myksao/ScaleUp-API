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

opinion = Opinion.Opinion()

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
        if len(sector) != 0:
            getsector = opinion.switch_collection(Opinion.opinions(sector=sector))
        
            checkbill =QuerySet(opinion, getsector._get_collection()).get(place=place)
        
            return checkbill
        else:
            return {'message':'No Sector Sent','status':500}
        
        


    @staticmethod
    async def resolve_chat(sector, place, _id):
        
     
        if len(_id)!=0:
            if len(sector)!=0:
                getsector = opinion.switch_collection(Opinion.opinions(sector=sector))
                opinionchat =QuerySet(opinion, getsector._get_collection()).get(_id=_id, place=place)
                eachchat = json.loads(opinionchat.to_json())
                for messagechat in eachchat['message']:
                    await map(chatimage, messagechat) 
                return eachchat
            else:
                return {'message':'No Sector Sent','status':500}
        else:
            return {'response': 'No chatid error'}
        #Can't be empty , just trying to avoid nullpointerexpection .....

    @staticmethod
    async def resolve_user(password,imei):
        checkimei =  User.User.objects(imei__contains=imei)
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
    async def resolve_state():
        try:
            getall = await StateLocal.StateLocal.objects()
            return getall
        except Exception:
            print('Ooops No Data')

    @staticmethod
    async def resolve_stalga(name):
        try:
            getall = StateLocal.StateLocal.objects(name__contains=name)
            return getall
        except Exception:
            print('Ooops No Data')
    
    @staticmethod
    async def resolve_articles():
        try:
            articlelist = await Article.Article.objects()
            return articlelist
        except Exception:
            print('Ooops No Data')
    
    @staticmethod
    async def resolve_article(title):
        try:
            article = await Article.Article.objects(title__contains = title)
            return article
        except Exception:
            print('Ooops No Data')
    
    

    @staticmethod
    async def resolve_complains():
        try:
            complainpost = await Complain.Complain.objects()
            eachpost = json.loads(complainpost.to_json())
            for post in eachpost:
              await  list(map(chatimage,post['images']))

            return eachpost
        except Exception:
            print('Ooops No Data')
    
    @staticmethod
    async def  resolve_complain(_id):
        try:
            getcomplain = await Complain.Complain.objects(_id__contains = Int(_id))
            return getcomplain
        except Exception:
            print('Ooops No Data')
        

    @staticmethod
    async def resolve_constitutions():
        try:
            constitutions = await Constitution.Constitution.objects()
            return constitutions
        except Exception:
            print('Ooops No Data')
        
    @staticmethod
    async def resolve_constitution(id):
        try:
            constitution = await Constitution.Constitution.objects(id__match = id)
            return constitution
        except Exception:
            print('Ooops No Data')
        

   

                


                


