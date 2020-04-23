
from ariadne import SubscriptionType
import asyncio
from src.broadcast import broadcast

subscription = SubscriptionType()


@subscription.source('chat')
async def chat_generator(obj,info,_id):
        await broadcast.connect()
        async with broadcast.subscribe(channel=_id) as subscriber:
                async for event in subscriber:
                        # print(event)
                        yield event

@subscription.field('chat')
def chat_resolver(obj,info,_id):
        # print(_id)
        # print(obj.message)
        return obj


