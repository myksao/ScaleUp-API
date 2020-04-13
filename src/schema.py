from graphene import ObjectType,Schema
from src.operation import query,mutation,subscription
from src.models import types


# ,subscription= subscription.RootSubscription 
schema = Schema(query= query.RootQuery,mutation= mutation.RootMutation,types=[types.TOpinion,types.TThumbUp,types.TThumbUp,types.TSubArticle,types.TState,types.TUser,types.TConstitution,types.TArticle,types.TComplain,types.TMessage,types.TStateLocal,types.TUser])
 


