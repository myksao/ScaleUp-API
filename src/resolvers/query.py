#convert image to base64
import base64
# You might also find it useful to create python dictionaries
import json
import os
# decrypt password
from cryptography.fernet import Fernet
from dotenv import load_dotenv

from ariadne import QueryType

# Mongodb schema
from src.model import Opinion,StateLocal,Complain,Article,Constitution,User
from mongoengine.queryset.queryset import QuerySet
from mongoengine.queryset.visitor import Q

load_dotenv()
opinion = Opinion.Opinion
# ariadne
query = QueryType()


#convert binary file from the mongodb to base64
def chatimage(eachimage):
    message_bytes = base64.b64encode(eachimage.encode('ascii'))
    base64_message = message_bytes.decode('ascii')
    return base64_message


@query.field('bills')
async def resolve_bills(obj,info,sector, place):
    sectorname = await Opinion.opinions(sector=sector)

    if sector != None:
        # result =  opinion.objects.get(place=place).switch_collection('health')
        # print(result)
        getsector = opinion.switch_collection(opinion(),sectorname)
        # print(getsector._get_collection())
        checkbill =QuerySet(opinion, getsector._get_collection())
        result = checkbill.filter(place=place)
        return result
    else:
        return {'message':'No Sector Sent','status':500}
    
        
@query.field('chat')
async def resolve_chat(parent,info,sector, place, _id):
    sectorname = await Opinion.opinions(sector=sector)
    getsector = opinion.switch_collection(opinion(),sectorname)
    chat = QuerySet(opinion, getsector._get_collection())
            
    if _id!=None:
        if sector!=None:
            response = chat(Q(_id=_id)& Q(place=place)).first()
            # eachchat = json.loads(result.to_json())
            # for messagechat in eachchat['message']:
            #     await map(chatimage, messagechat) 
            return response
        else:
            return {'message':'No Sector Sent','status':500}
    else:
        return {'response': 'No chatid error'}
    #Can't be empty , just trying to avoid nullpointerexpection .....

@query.field('user')
async def resolve_user(parent,info,password,imei):
    checkimei =  User.User.objects(imei=imei)
    if len(checkimei) != 0:
        key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
        ciphered_password = Fernet(key).decrypt(password.encode())
        if(ciphered_password == checkimei.password):
            return checkimei
        else:
            message = {'response':'Incorrect Password'}
            return message
    else:
        message = {'response':'Not registered'}
        return message

@query.field('state')
async def resolve_state(parent,info):
    try:
        getall = StateLocal.StateLocal.objects
        return getall
    except Exception:
        print('Ooops No Data')

@query.field('stalga')
async def resolve_stalga(parent,info,name):
    try:
        getall = StateLocal.StateLocal.objects(state__name=name).first()
        return getall
    except Exception:
        print('Ooops No Data')

@query.field('articles')
async def resolve_articles(parent,info):
    try:
        articlelist = Article.Article.objects
        return articlelist
    except Exception:
        print('Ooops No Data')

@query.field('article')
async def resolve_article(parent,info,title):
    try:
        article = Article.Article.objects(title=title).first()
        return article
    except Exception:
        print('Ooops No Data')


@query.field('complains')
async def resolve_complains(parent,info):
    try:
        complainpost =  Complain.Complain.objects
        # eachpost = json.loads(complainpost.to_json())
        # for post in eachpost:
        #     await  list(map(chatimage,post['images']))

        return complainpost
    except Exception:
        print('Ooops No Data')

@query.field('complain')
async def  resolve_complain(parent,info,_id):
    try:
        getcomplain =  Complain.Complain.objects(_id = Int(_id)).first()
        return getcomplain
    except Exception:
        print('Ooops No Data')
    

@query.field('constitutions')
async def resolve_constitutions(parent,info):
    try:
        constitutions =  Constitution.Constitution.objects
        return constitutions
    except Exception:
        print('Ooops No Data')
    
@query.field('constitution')
async def resolve_constitution(parent,info,id):
    try:
        constitution = Constitution.Constitution.objects(section__id=id).first()
        return constitution
    except Exception:
        print('Ooops No Data')
    



            


            


