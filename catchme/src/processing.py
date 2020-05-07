# processing dataset from raw i.e cleaning dataset set from stopwords,regex and all
# then forward it to processed folder
import csv
from pathlib import  Path
import spacy
from spacy.matcher import Matcher
from spacy.lang.en import English
from spacy.tokens import Doc
import  re
import json
from spacy.symbols import ORTH
from catchme.helper.helper import pron_expections,clean


class Processing:      

    @staticmethod
    async def process_raw_data():
        nlp = spacy.load('en_core_web_md')
        # nlp = English()
        nlp.add_pipe(clean,first=True)

        # print(nlp.pipe_names)
        await pron_expections(nlp,'i','did','do','you','does','it','could','that')
        
        processed_data=[]
        fieldnames = ['text','sentiment']
        for  child in Path('catchme/data/raw/').glob('*.json'):
            
            with open('catchme/data/raw/Sentiment.json','r') as json_data:
                raw = json.load(json_data)
                with open(child.name,'w',) as processed:
                    for row in raw:
                        doc = nlp(row['text']) #input the text
                        
                        # print(doc.text)
                #         for token in doc:
                #             if token.text == span:
                #                 # token = ''
                #                 print(token.doc)
                #                 processed_data.extend([{'text':token.sent,'sentiment':row['sentiment']}])
                # processed.write(json.dumps(processed_data, indent=4, sort_keys=False,separators=(',',':')))





            
# print(re.match('^@[\w\W]+.$',"@lkwdcitizen:"))
# print(re.findall(R'''(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))''',"RT @BradBannon: Was GOP Debate a Campaign Preview or Rearview? by @BradBannon on @LinkedIn https://t.co/n0mko8qQIE #UniteBlue #P2 #POTUS â€¦"))
# print([i for i in re.finditer(R'#\w*[a-zA-Z]+\w*|@(\w+|\W+)[:]?|(RT)+[:]?','RT: rt RT T-Mobile @ali: Lots of Republicans in my Facebook and Twitter timelines are ticked at Fox News for running that hatchet job of a debate. #GOPdebaâ€¦')])
# (See all on my http://t.co/MOcgZtHBdZ site.)
# http://tâ€¦
# (http://t.co/k7RBb12RLC)

# RT @BradBannon: "Was GOP Debate a Campaign Preview or Rearview?" by @BradBannon on @LinkedIn https://t.co/n0mko8qQIE #UniteBlue #P2 #POTUS â€¦
# RT @ali: Lots of Republicans in my Facebook and Twitter timelines are ticked at Fox News for running that hatchet job of a debate. #GOPdebaâ€¦