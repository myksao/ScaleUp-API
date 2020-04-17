import os
from dotenv import load_dotenv
from mongoengine import connect
from ariadne import load_schema_from_path,make_executable_schema, upload_scalar
from ariadne.asgi import GraphQL
from src.resolvers import query,mutation,subscription
import uvicorn 
from src.broadcast import broadcast

import asyncio

load_dotenv()



database = os.getenv('DB_CONNECTION')

# print(database)

# connect to mongodb
connect(host=database)



# Load schema from file...
type_defs = load_schema_from_path('src/model/schema.graphql')


# Build an executable schema
schema = make_executable_schema(type_defs,[query.query,mutation.mutation,subscription.subscription,upload_scalar])

# Create an ASGI app for the schema
app = GraphQL(schema)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
