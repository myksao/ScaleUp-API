from graphene import ObjectType,Schema
from src.operation import query,mutation,subscription



# ,subscription= subscription.RootSubscription 
schema = Schema(query= query.RootQuery,mutation= mutation.RootMutation)
 


