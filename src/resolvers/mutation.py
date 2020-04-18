# You might also find it useful to create python dictionaries
import json
import os
import asyncio
# decrypt password
from cryptography.fernet import Fernet
from dotenv import load_dotenv

from ariadne import MutationType

# Mongodb schema and Graphene Type Def
from src.model import Opinion,StateLocal,Complain,Article,Constitution,User
# call the queryset to get data from mongo
from mongoengine.queryset.queryset import QuerySet
from mongoengine.queryset.visitor import Q
from src.broadcast import broadcast
load_dotenv()

opinion = Opinion.Opinion
ThumbsUp = Opinion.ThumbUp
ThumbsDown = Opinion.ThumbDown
Message = Opinion.Message
userobject = User.User
complain = Complain.Complain


mutation = MutationType()
# Add Bill/Opinion
@mutation.field('addbill')
async def resolve_addbill(obj,info,bill,sector,place,thumbsup,thumbsdown):
    sectorname = await Opinion.opinions(sector=sector)
    getsector = opinion.switch_collection(opinion(),sectorname)
    checkbill = QuerySet(opinion,getsector._get_collection())
    result = checkbill.filter(Q(bill=bill) & Q(place=place)).first()
    
    if result!=None:
        message = "Bill already exist , search for it and give your peaceful opinion"
        return {"message":message,"status":500}
    else:
        try:  
            sectorname = await Opinion.opinions(sector=sector)

            opinionentry =  opinion(place=place,bill=bill,thumbsup = ThumbsUp(noofvote=thumbsup),thumbsdown=ThumbsDown(noofvote=thumbsdown))
            opinionentry.switch_collection(sectorname)
            opinionentry.save()
            opinionresponse = opinionentry['bill']
            message = f'{opinionresponse} Bill Added For Discussion'
            return {"message": message,"status":200}
        except Exception as error:
            return {'message':f'Error {error}','status':500}



# Chat fpr each Bill/Opinion
@mutation.field('addchat')
async def resolve_addchat(obj,info,_id,place,messageid,text,image,delivered,timestamp,user,sector):

    if sector!=None:
        # if len(image)==0:
        try:
            sectorname = await Opinion.opinions(sector=sector)
            getsector = opinion.switch_collection(opinion(),sectorname)
            room = QuerySet(opinion,getsector._get_collection())
            add_chat_to_rooms = room(id=_id,place=place).update_one(push__message=Message(    
                billid=_id,
                messageid=messageid,
                text= text,
                image = image,
                delivered=delivered,
                timestamp= timestamp,
                user= user   
            ))
            
            await broadcast.connect()
            await broadcast.publish(channel=_id, message=Message(    
                billid=_id,
                messageid=messageid,
                text= text,
                image = image,
                delivered=delivered
                timestamp= timestamp,
                user= user   
            ))

            if add_chat_to_rooms==1:
                # perform asubscription here
                return {'message':'Message Uploaded','status':200}
            else:
                return {'message':'Error Uploading Message','status':100}
            
        except Exception as error:
            return {'message':f'An exception occured {error}','status':500}
        # else:
        #     try:
        #         sectorname = await Opinion.opinions(sector=sector)
        #         getsector = opinion.switch_collection(opinion(),sectorname)
        #         room = QuerySet(opinion,getsector._get_collection())
        #         # opinion.switch_collection(opinion(),sectorname)
        #         add_chat_to_rooms = room(id=_id,place=place).update_one(push__message=Message(
        #             billid=_id,messageid= messageid,text=text,image= image,timestamp= timestamp,user= user   
        #         ))

        #         print(add_chat_to_rooms)
                
        #         if add_chat_to_rooms==1:
        #             # perform asubscription here
        #             return {'message':'Message Uploaded','status':200}
        #         else:
        #             return {'message':'Error Uploading Message','status':100}
        #     except Exception as error:
        #         return {'message':f'An exception occured {error}','status':500}
    else:
        return {'message':'No Sector Sent','status':500}



# Add Vote For Each Bill/Opinion room
@mutation.field('addvote')
async def resolve_addvote(root,info,_id,place,sector,user):

    sectorname = await Opinion.opinions(sector=sector)
    getsector = opinion.switch_collection(opinion(),sectorname)
    vote = QuerySet(opinion, getsector._get_collection())
            
    if sector!=None:
        try:
            response = vote(Q(id=_id)&Q(place=place)&Q(thumbsdown__votersid=user)).first()

            print(response)
            if response==None:
                response = vote(Q(id=_id)&Q(place=place)&Q(thumbsup__votersid=user)).first()
                print(response)
                if response==None:
                    updatethumbsup = vote(Q(id=_id)&Q(place=place)).update_one(push__thumbsup__votersid=user,inc__thumbsup__noofvote=1)

                    if updatethumbsup==1:
                        return {'message':'Congrat, your vote has been accepted','status':200}
                    
                else:
                    return {'message':'You have voted already','status':200}
                    

            else:
                deleteidthumbsdown = vote(Q(id=_id)&Q(place=place)).update_one(pull__thumbsdown__votersid=user,dec__thumbsdown__noofvote=1)
                
                
                if deleteidthumbsdown==1:
                    response = vote(Q(id=_id)&Q(place=place)&Q(thumbsup__votersid__=user)).first()

                    if response==None:
                        updatethumbsup = vote(Q(id=_id)&Q(place=place)).update_one(push__thumbsup__votersid=user,inc__thumbsup__noofvote=1)
                        if updatethumbsup==1:
                            return {'message':'Congrat, your vote has been accepted','status':200}
                        
                    else:
                        return {'message':'You have voted already','status':200}

        except Exception as error:
            return {'message':f'An error occured {error}','status':500}
    else:
        pass


# Remove Vote For Each Bill/Opinion room
@mutation.field('removevote')
async def resolve_removevote(obj,info,_id,place,sector,user):
    sectorname = await Opinion.opinions(sector=sector)
    getsector = opinion.switch_collection(opinion(),sectorname)
    vote = QuerySet(opinion, getsector._get_collection())
    
    if sector!=None:
        try:
            response = vote(Q(id=_id)&Q(place=place)&Q(thumbsup__votersid=user)).first()
            print(response)
            if response==None:
                response = vote(Q(id=_id)&Q(place=place)&Q(thumbsdown__votersid=user)).first()

                if response==None:
                    updatethumbsdown = vote(Q(id=_id)&Q(place=place)).update_one(push__thumbsdown__votersid=user,inc__thumbsdown__noofvote=1)
                    
                    if updatethumbsdown==1:
                        return {'message':'Congrat, your vote has been accepted','status':200}
                    
                else:
                    return {'message':'You have voted already','status':200}

                
            else:
                print('here')
                deleteidthumbsup = vote(Q(id=_id)&Q(place=place)).update_one(pull__thumbsup__votersid=user,dec__thumbsup__noofvote=1)

                if deleteidthumbsup==1:
                    response = vote(Q(id=_id)&Q(place=place)&Q(thumbsdown__votersid=user)).first()

                    if response ==None:
                        updatethumbsdown = vote(Q(id=_id)&Q(place=place)).update_one(push__thumbsdown__votersid=user,inc__thumbsdown__noofvote=1)

                        if updatethumbsdown==1:
                            return {'message':'Congrat, your vote has been accepted','status':200}
                        
                    else:
                        return {'message':'You have voted already','status':200}   

        except Exception:
            return {'message':'An error occured','status':500}
    else:
        pass
    

# Add User  
@mutation.field('adduser')
async def resolve_adduser(obj,info,imei,name,userid,password,email,state,placer,placeo,telephone):
    
    
        # Validate user
    imeicheck =  userobject.objects(imei=imei)

    if len(imeicheck) != 0:
        
        return {'message':'You have registered this device','status':200}
    else:
        try:
            key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
            ciphered_password = Fernet(key).encrypt(password.encode())

            registeruser = userobject(
                imei=imei,
                name=name,
                userid=userid,
                password=ciphered_password,
                email=email,
                state=state,
                placeofresidence=placer,
                placeoforigin=placeo,
                telephone=telephone
            ).save()
            # print(registeruser)
            return {'message':f'Welcome {name}','status':200}
        
        except Exception:

            return {'message':'An error occured','status':500}

# Add Complains
@mutation.field('addcomplain')
async def resolve_addcomplain(root,info,post,image):
    
    # if int(id)==0:

    try:
        storecomplain = complain(post=post,images=[image]).save()
            # subscription
        # print(storecomplain)
        if storecomplain!=None:
            return {'message':'Post Uploaded','status':200}
        else:
            return {'message':'Error Uploading Message','status':100}
    except Exception:
        return {'message':'An Error occured','status':500}
    # else:
    #     try:
    #         imgcomplain = complain.objects(id=_id).update(push__images=image).save()
            
    #         # subscription
        # except Exception:
        #     return {'message':'An error occured','status':500}

