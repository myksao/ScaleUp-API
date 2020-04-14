
from graphene import ObjectType,Field,JSONString,Int,Float
from src.models import types
import asyncio







class RootSubscription(ObjectType):

    countto = Field(Float(),up_to=Int())

    @staticmethod
    async def resolve_countto(root,info,up_to):
        for i in range(up_to):
            yield i
            await asyncio.sleep(1.)
        yield up_to


    # @staticmethod
    # def resolve_chat(_id):
    #     pass
    


