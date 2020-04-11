import os
from dotenv import load_dotenv
from mongoengine import connect
from src.schema import schema
from sanic import Sanic
from sanic_graphql import GraphQLView
from graphql_ws.websockets_lib import WsLibSubscriptionServer
from graphql.execution.executors.asyncio import AsyncioExecutor

load_dotenv()

database = os.getenv('DB_CONNECTION')

print(database)

# connect to mongodb
connect(host=database)

# start sanic async web server
app = Sanic(__name__)

@app.listener('before_server_start')
def init_graphql(app, loop):
    app.add_route(GraphQLView.as_view(schema=schema, executor=AsyncioExecutor(loop=loop)), '/graphql')


subscription_server = WsLibSubscriptionServer(schema)


@app.websocket('/subscriptions', subprotocols=['graphql-ws'])
async def subscriptions(request, ws):
    await subscription_server.handle(ws)
    return ws

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337,)



