from graphene import ObjectType,Schema
from src.operation import query,mutation,subscription
from src.models import types


# ,subscription= subscription.RootSubscription 
schema = Schema(query= query.RootQuery,mutation= mutation.RootMutation,types=[types.TMessage])
 


