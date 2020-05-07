# using different kind of machine learning algorithm trainer to train based on dataset 
# usually classifiers 
# after training store to pickle in a increment style
# then forward it to model folder

from pathlib import Path
from spacy.util import minibatch
import spacy
import random
import csv
class Modeling:
    def __call__(self):
        self.nlp = spacy.blank('en')
        self.textcat = self.nlp.create_pipe(
            "textcat", config={"exclusive_classes": True, "architecture": "simple_cnn"}
        )
        self.nlp.add_pipe(textcat, last=True)

         # add label to text classifier
        self.textcat.add_label("Positive")
        self.textcat.add_label("Negative")
        self.textcat.add_label("Neutral")

    async def training_sentimental_model(self):
        traning_data = []
        for  child in Path('catchme/data/processed/').glob('*.csv'):
            with open(child,'rt',newline='') as processed:
                reader = csv.DictReader(processed)
                for row in reader:
                    traning_data.append(row['text'],row['label'])


                   
        optimizer= nlp.being_training()

        for train in range(20):
            random.shuffle(traning_data)

            for batch in minibatch(traning_data,size=50000):

                text,annotations= zip(*batch)

                self.nlp.update(text,annotations,sgd=optimizer)

                #save to disk i.e. model folder afterwards 
