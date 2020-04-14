
from graphene import ObjectType,Field,JSONString,Int
from src.models import types
import asyncio







class RootSubscription(ObjectType):

    count =  Field(up=Int)

    async def resolve_count(root,info,up):
        for i in range(up):
            yield i
            await asyncio.sleep(1.)
        yield up


    # @staticmethod
    # def resolve_chat(_id):
    #     pass
    


