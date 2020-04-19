from ariadne import UnionType
from src.model import User,UserFailedResponse
error = UnionType("UserResult")

@error.type_resolver
def resolve_error_type(obj, *_):
    # print(obj)
    if isinstance(obj,User.User):
        return 'User'
    if isinstance(obj,UserFailedResponse.UserFailedResponse):
        return 'UserFailedResponse'
    return None
    
