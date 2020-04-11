import os
from sanic import Sanic
from sanic_graphql import GraphQLView
from graphql_ws.websockets_lib import WsLibSubscriptionServer

from dotenv import load_dotenv
from mongoengine import connect
from src.schema import schema

load_dotenv()

database = os.getenv('DB_CONNECTION')

print(database)

# connect to mongodb
connect(host="mongodb+srv://scaleup:0KNarIAz88He1QPH@scaleup-agf7c.mongodb.net/scaleup?retryWrites=true&w=majority")

# start sanic async web server
app = Sanic(__name__)

app.add_route(GraphQLView.as_view(schema=schema, graphiql=True), '/graphql')


subscription_server = WsLibSubscriptionServer(schema)


@app.websocket('/subscriptions', subprotocols=['graphql-ws'])
async def subscriptions(request, ws):
    await subscription_server.handle(ws)
    return ws


app.run(host="0.0.0.0", port=8000)


