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
subscription_server = WsLibSubscriptionServer(schema)

# Middleware can be added just like js middlewares to modify the request to or response 
# Listeners helps to execute startup/teardown code as your server starts or closes  
@app.listener('before_server_start')
@app.websocket('/subscriptions', subprotocols=['graphql-ws'])
async def init_graphql(app,loop):
    app.add_route(GraphQLView.as_view(schema=schema,executor= AsyncioExecutor(loop=loop), graphiql=True),'')
    await subscription_server.handle(ws)
    return ws



# @app.websocket('/subscriptions', subprotocols=['graphql-ws'])
# async def subscriptions(request, ws):
#     await subscription_server.handle(ws)
#     return ws

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337,)



