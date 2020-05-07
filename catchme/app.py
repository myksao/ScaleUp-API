# Perfom all operation on all classifier pickle i,e custom classifier for a mode range

from catchme.src.preparation import Preparation
from catchme.src.processing import Processing
from catchme.src.modeling import Modeling
import asyncio
from enum import Enum


async def train(*path,custom_sentiment:str):
   # await Preparation(path,custom_sentiment=custom_sentiment).new_imported_data()
   await Processing().process_raw_data()
   #await Modeling().training_sentimental_model()



# async def test(message:str):
#     #load model to spacy
#     # add message to nlp spacy
#     #get response

if __name__ == '__main__':
    asyncio.run(train(
       'C:\Guess\Data\Tweets.csv',
       custom_sentiment=None))

