import os
from dotenv import load_dotenv
from mongoengine import connect
from src.schema import schema
from sanic import Sanic
from sanic_graphql import GraphQLView
from graphql.execution.executors.asyncio import AsyncioExecutor
from graphql_ws.websockets_lib import WsLibSubscriptionServer

load_dotenv()

database = os.getenv('DB_CONNECTION')

# print(database)

# connect to mongodb
connect(host=database)

# start sanic async web server
app = Sanic(__name__)

# Middleware can be added just like js middlewares to modify the request to or response 
# Listeners helps to execute startup/teardown code as your server starts or closes  
# @app.listener('before_server_start')
# def init_graphql(app,loop):
#     app.add_route(GraphQLView.as_view(schema=schema,executor= AsyncioExecutor(loop=loop), graphiql=True),'')


subscription_server = WsLibSubscriptionServer(schema)

@app.listener('before_server_start')
async def init_graphql(app,loop,request, ws):
    app.add_websocket_route(GraphQLView.as_view(schema=schema,executor= AsyncioExecutor(loop=loop), graphiql=True),'',subprotocols=['graphql-ws'])
    await subscription_server.handle(ws)
    return ws



# @app.websocket('/subscriptions', subprotocols=['graphql-ws'])
# async def subscriptions(request, ws):
#     await subscription_server.handle(ws)
#     return ws

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337,)



