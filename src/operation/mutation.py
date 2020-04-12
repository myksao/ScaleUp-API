# You might also find it useful to create python dictionaries
import json
import os
import asyncio
# decrypt password
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from graphene import Mutation,ObjectType,Field,Int,String,List,NonNull
# Upload File image
from graphene_file_upload.scalars import Upload
# Mongodb schema and Graphene Type Def
from src.models import Opinion,StateLocal,Complain,Article,Constitution,User,types
# call the queryset to get data from mongo
from mongoengine.queryset.queryset import QuerySet

load_dotenv()
cryptkey = os.getenv('key')

opinion = Opinion.Opinion
ThumbsUp = Opinion.ThumbUp
ThumbsDown = Opinion.ThumbDown
Message = Opinion.Message
userobject = User.User
complain = Complain.Complain


# Add Bill/Opinion
class AddBill(Mutation):
    class Arguments:
        bill=NonNull(String)
        sector=NonNull(Int)
        place=NonNull(String)
        thumbsup=NonNull(Int)
        thumbsdown=NonNull(Int)

    message=String()
    status=Int()

    async def mutate(root,info,bill,sector,place,thumbsup,thumbsdown):

        checkbill = ''

        sectorname = await Opinion.opinions(sector=sector)
        getsector = opinion.switch_collection(opinion(),sectorname)
        checkbill = QuerySet(opinion,opinion._get_collection(),getsector)
        checkbill(Q(bill=bill) & Q(place=place))

        if len(checkbill)!=0:
            message = "Bill already exist , search for it and give your peaceful opinion"
            return AddBill(message=message,status=500)
        else:
            try:  
                sectorname = await Opinion.opinions(sector=sector)

                opinionentry =  opinion(place=place,bill=bill,thumbsup = ThumbsUp(noofvote=thumbsup),thumbsdown=ThumbsDown(noofvote=thumbsdown))
                opinionentry.switch_collection(sectorname)
                opinionentry.save()
                opinionresponse = opinionentry['bill']
                message = f'{opinionresponse} Bill Added For Discussion'
                return AddBill(message= message,status= 200)
            except Exception:
                return AddBill(message='Error',status=500)





# Chat fpr each Bill/Opinion
class AddChat(Mutation):
    class Arguments:
        _id=NonNull(String)
        place=NonNull(String)
        id= NonNull(Int)
        text=String()
        filepath= Upload()
        filetype= String()
        timestamp= NonNull(String)
        user=NonNull(String)
        sector=NonNull(Int)
    
    message=String()
    status=Int()

    async def mutate(root,info,_id,place,id,text,filepath,filetype,timestamp,user,sector):
        
        if sector!=None:
            if not filepath:
                try:
                    sectorname = await Opinion.opinions(sector=sector)

       
                    add_chat_to_rooms = opinion(Q(_id=_id)&Q(place=place)).update(push_all__message=[{
                    'billid':_id,
                    'id': id,
                    'text': text,
                    'timestamp': timestamp,
                    'user': user   
                    }])
                    add_chat_to_rooms.switch_collection(sectorname)
                    add_chat_to_rooms.save()

                    if len(add_chat_to_rooms)!=0:
                        # perform asubscription here
                        return AddChat(message='Message Uploaded',status=200)
                    else:
                        return AddChat(message='Error Uploading Message',status=100)
                    return 
                   
                except Exception:
                    return AddChat(message='An exception occured',status=500)
            else:
                try:
                    sectorname = await Opinion.opinions(sector=sector)

                    add_chat_to_rooms = opinion(Q(_id=_id)&Q(place=place)).update(push_all__message=[{
                    'billid':_id,
                    'id': id,
                    'image': Opinion.Message().image.put(filepath,content_type=filetype),
                    'timestamp': timestamp,
                    'user': user   
                    }])

                    add_chat_to_rooms.switch_collection(sectorname)
                    add_chat_to_rooms.save()

                    if len(add_chat_to_rooms)!=0:
                        # perform asubscription here
                        return AddChat(message='Message Uploaded',status=200)
                    else:
                        return AddChat(message='Error Uploading Message',status=100)
                    return 
                   
                except Exception:
                    return AddChat(message='An exception occured',status=500)
        else:
            return AddChat(message='No Sector Sent',status=500)



# Add Vote For Each Bill/Opinion room
class AddVote(Mutation):
    class Arguments:
        _id=NonNull(String)
        place=NonNull(String)
        sector=NonNull(Int)
        user = NonNull(String)

    message=String()
    status=Int()

    def mutate(root,info,_id,place,sector,user):

        if sector!=None:
            try:
                sectorname = await Opinion.opinions(sector=sector)
                getsector = opinion.switch_collection(opinion(),sectorname)
                checkdownvote = QuerySet(opinion, getsector._get_collection())
                checkdownvote(Q(_id=id)&Q(place=place)&Q(thumbsdown__votersid__match =user))

                if len(checkdownvote)!=0:
                    deleteidthumbsdown = opinion(Q(_id=id)&Q(place=place)).update(pull__thumbsdown__votersid=user,inc__thumbsdown__noofvote=-1)
                    deleteidthumbsdown.switch_collection(sectorname)
                    deleteidthumbsdown.save()
                    
                    if len(deleteidthumbsdown)!=0:
                        getsector = opinion.switch_collection(opinion(),sectorname)
                        checkupvote = QuerySet(opinion, getsector._get_collection())
                        checkupvote(Q(_id=id)&Q(place=place)&Q(thumbsup__votersid__match =user))

                        if len(checkupvote)==0:
                            updatethumbsup = opinion(Q(_id=id)&Q(place=place)).update(pull__thumbsup__votersid=user,inc__thumbsup__noofvote=1)
                            updatethumbsup.switch_collection(sectorname)
                            updatethumbsup.save()
                            if len(updatethumbsup)!=0:
                                return AddVote(message='Congrat, your vote has been accepted',status=200)
                            
                        else:
                            return AddVote(message='You have voted already',status=200)

                else:
                    getsector = opinion.switch_collection(opinion(),sectorname)
                    checkupvote = QuerySet(opinion, getsector._get_collection())
                    checkupvote = opinion.objects(Q(_id=id)&Q(place=place)&Q(thumbsup__votersid__match =user))

                    if len(checkupvote)==0:
                        updatethumbsup = opinion(Q(_id=id)&Q(place=place)).update(push__thumbsup__votersid=user,inc__thumbsup__noofvote=1)
                        updatethumbsup.switch_collection(sectorname)
                        updatethumbsup.save()

                        if len(updatethumbsup)!=0:
                            return AddVote(message='Congrat, your vote has been accepted',status=200)
                        
                    else:
                        return AddVote(message='You have voted already',status=200)



            except Exception:
                return AddVote(message='An error occured',status=500)
        else:
            pass





class RemoveVote(Mutation):
    class Arguments:
        _id=NonNull(String)
        place=NonNull(String)
        sector=NonNull(Int)
        user=NonNull(String)

    message=String()
    status=Int()

    def mutate(root,info,_id,place,sector,user):
        try:
            sectorname = await Opinion.opinions(sector=sector)
            getsector = opinion.switch_collection(opinion(),sectorname)
            checkupvote = QuerySet(opinion, getsector._get_collection())
            checkupvote(Q(_id=id)&Q(place=place)&Q(thumbsup__votersid__match =user))
            
            if len(checkupvote)!=0:
                deleteidthumbsup = opinion(Q(_id=id)&Q(place=place)).update(pull__thumbsup__votersid=user,inc__thumbsup__noofvote=-1)
                deleteidthumbsup.switch_collection(sectorname)
                deleteidthumbsup.save()

                if(deleteidthumbsup):
                    getsector = opinion.switch_collection(opinion(),sectorname)
                    checkdownvote = QuerySet(opinion, getsector._get_collection())
                    checkdownvote(Q(_id=id)&Q(place=place)&Q(thumbsdown__votersid__match =user))

                    if len(checkdownvote)==0:
                        updatethumbsdown = opinion(Q(_id=id)&Q(place=place)).update(push__thumbsdown__votersid=user,inc__thumbsdown__noofvote=1)
                        updatethumbsdown.switch_collection(sectorname)
                        updatethumbsdown.save()

                        if len(updatethumbsdown)!=0:
                            return RemoveVote(message='Congrat, your vote has been accepted',status=200)
                       
                    else:
                        return RemoveVote(message='You have voted already',status=200)
            else:
                getsector = opinion.switch_collection(opinion(),sectorname)
                checkdownvote = QuerySet(opinion, getsector._get_collection())
                checkdownvote(Q(_id=id)&Q(place=place)&Q(thumbsdown__votersid__match =user))

                if len(checkdownvote)==0:
                    updatethumbsdown = opinion.objects(Q(_id=id)&Q(place=place)).update(push__thumbsdown__votersid=user,inc__thumbsdown__noofvote=1)
                    updatethumbsdown.switch_collection(sectorname)
                    updatethumbsdown.save()
                    
                    if len(updatethumbsdown)!=0:
                        return RemoveVote(message='Congrat, your vote has been accepted',status=200)
                   
                else:
                    return RemoveVote(message='You have voted already',status=200)
            

        except Exception:
            return RemoveVote(message='An error occured',status=500)
        


class AddUser(Mutation):
    class Arguments:
        imei=NonNull(String)
        name=NonNull(String)
        userid=String()
        password=String()
        email=String()
        state=String()
        placer=String()
        placeo=String()
        telephone=String()

    message=String()
    status=Int()

    def mutate(root,info,imei,name,userid,password,email,state,placer,placeo,telephone):
       
      
         # Validate user
        imeicheck =  userobject.objects(imei=imei)

        if len(imeicheck) != 0:
            
            return AddUser(message='You have registered this device',status=200)
        else:
            try:
                cipher_suite = Fernet(cryptkey)
                ciphered_password = cipher_suite.encrypt(password)

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

                return AddUser(message=f'Welcome {name}',status=200)
            
            except Exception:

                return AddUser(message='An error occured',status=500)
    


class AddComplain(Mutation):
    class Arguments:
        id=Int()
        _id= String()
        post=String()
        filepath=Upload()
        filetype=String()

    message=String()
    status=Int()

    def mutate(root,info,id,_id,post,filepath,filetype):
        
        if int(id)==0:

            try:
                storecomplain = complain(post=post).save()
                
                 # subscription
                if len(storecomplain)!=0:
                    return AddComplain(message='Post Uploaded',status=200)
                    
            except Exception:
                return AddComplain(message='An Error occured',statsu=500)
        else:
            try:
                imgcomplain = complain.objects(_id=_id).update(push__images=Opinion.Message().image.put(filepath,content_type=filetype)).save()
                
                # subscription
            except Exception:
                return AddComplain(message='An error occured',status=500)







class RootMutation(ObjectType):

    addbill = AddBill.Field()
    addchat = AddChat.Field()
    addvote = AddVote.Field()
    removevote = RemoveVote.Field()
    adduser = AddUser.Field()
    addcomplain = AddComplain.Field()
