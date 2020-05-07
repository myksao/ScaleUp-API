import spacy
from spacy.symbols import ORTH
import re
from spacy.tokens import Doc

async def pron_expections(nlp,*case):
    for pron in [*case]:
        for contraction in [pron,pron.title()]:
            if re.match('(a|A)(re)',contraction):
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)
            
            elif re.match('((c|C)(annot))|((c|C)(an))',contraction):
                
                if contraction in ('can',"Can't"):
                    # can't
                    not_case=[{ORTH:contraction},{ORTH:"not"}]
                    nlp.tokenizer.add_special_case(contraction.strip('n')+"n't",not_case)
                
                elif contraction in ("cannot","Cannot"):
                    # cannnot
                    not_case=[{ORTH:contraction.strip('not')},{ORTH:"not"}]
                    nlp.tokenizer.add_special_case(contraction,not_case)
            
            
            elif re.match('(c|C)(ould)',contraction):
                # couldn't
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)
            
            elif re.match('(d|D)(id)',contraction):
                # didn't
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)
            
            elif re.match('(d|D)(o)',contraction):
                # don't
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)
            
            elif re.match('(d|D)(oes)',contraction):
                # doesn't
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)
            
                
            elif re.match('(h|H)(e)',contraction):
                #he'd
                had_case=[{ORTH:contraction},{ORTH:"had"}]
                would_case=[{ORTH:contraction},{ORTH:"would"}]
                nlp.tokenizer.add_special_case(contraction+"'d",had_case)
                nlp.tokenizer.add_special_case(contraction+"'d",would_case)
            
                # he'll
                will_case= [{ORTH:contraction},{ORTH:"will"}]
                shall_case= [{ORTH:contraction},{ORTH:"shall"}]
                nlp.tokenizer.add_special_case(contraction+"'ll",will_case)
                nlp.tokenizer.add_special_case(contraction+"'ll",shall_case)
            
            elif re.match('(h|H)(ad|as|have)',contraction):
                # hadn't
                # hasn't
                # haven't
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)
            

            elif re.match('(i|I)',contraction):
                # i'd
                had_case=[{ORTH:contraction},{ORTH:"had"}]
                would_case=[{ORTH:contraction},{ORTH:"would"}]
                nlp.tokenizer.add_special_case(contraction+"'d",had_case)
                nlp.tokenizer.add_special_case(contraction+"'d",would_case)
            
                # i'll
                will_case= [{ORTH:contraction},{ORTH:"will"}]
                shall_case= [{ORTH:contraction},{ORTH:"shall"}]
                nlp.tokenizer.add_special_case(contraction+"'ll",will_case)
                nlp.tokenizer.add_special_case(contraction+"'ll",shall_case)
                
                # i'm
                am_case = [{ORTH:contraction},{ORTH:"am"}]
                nlp.tokenizer.add_special_case(contraction+"'m",am_case)
                

                # i've
                have_case = [{ORTH:contraction},{ORTH:"have"}]
                nlp.tokenizer.add_special_case(contraction+"'ve",have_case)
               
                
            elif re.match('(i|I)(s)',contraction):
                # isn't
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)
            

            elif re.match('(i|I)(t)',contraction):
                # it's
                is_case = [{ORTH:contraction},{ORTH:"is"}]
                # has_case = [{ORTH:contraction},{ORTH:"has"}]
                nlp.tokenizer.add_special_case(contraction+"'s",is_case)
                # nlp.tokenizer.add_special_case(contraction+"'s",has_case)
                
            
            elif re.match('(l|L)(et)',contraction):
                # let's
                is_case = [{ORTH:contraction},{ORTH:"is"}]
                nlp.tokenizer.add_special_case(contraction+"'s",is_case)
               

            elif re.match('(m|M)(ust)',contraction):
                # mustn't
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)
            

            elif re.match('(m|M)(ight)',contraction):
                # mightn't
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)
            

            elif re.match('(h|H)(ad)',contraction):
                # hadn't
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)
            


            elif re.match('(n|N)(eed)',contraction):
                # needn't
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)
            
            
            elif re.match('(s|S)(he)',contraction):
                # she'd
                had_case=[{ORTH:contraction},{ORTH:"had"}]
                would_case=[{ORTH:contraction},{ORTH:"would"}]
                nlp.tokenizer.add_special_case(contraction+"'d",had_case)
                nlp.tokenizer.add_special_case(contraction+"'d",would_case)
            
                # she's
                is_case = [{ORTH:contraction},{ORTH:"is"}]
                has_case = [{ORTH:contraction},{ORTH:"has"}]
                nlp.tokenizer.add_special_case(contraction+"'s",is_case)
                nlp.tokenizer.add_special_case(contraction+"'s",has_case)
                
            
            elif re.match('(s|S)(hould)',contraction):
                # shouldn't
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)
            
            
            elif re.match('(s|S)(all)',contraction):
                # shan't
                shallnot_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction.strip('hall')+"han't",shallnot_case)
            
            elif re.match('(t|T)(hat)',contraction):
                # that'll
                will_case= [{ORTH:contraction},{ORTH:"will"}]
                shall_case= [{ORTH:contraction},{ORTH:"shall"}]
                nlp.tokenizer.add_special_case(contraction+"'ll",will_case)
                nlp.tokenizer.add_special_case(contraction+"'ll",shall_case)
                
                #that'd 
                had_case=[{ORTH:contraction},{ORTH:"had"}]
                would_case=[{ORTH:contraction},{ORTH:"would"}]
                nlp.tokenizer.add_special_case(contraction+"'d",had_case)
                nlp.tokenizer.add_special_case(contraction+"'d",would_case)
            
                # that's
                is_case = [{ORTH:contraction},{ORTH:"is"}]
                has_case = [{ORTH:contraction},{ORTH:"has"}]
                nlp.tokenizer.add_special_case(contraction+"'s",is_case)
                nlp.tokenizer.add_special_case(contraction+"'s",has_case)
                
            
            elif re.match('(t|T)(here)',contraction):
                # there'll
                will_case= [{ORTH:contraction},{ORTH:"will"}]
                shall_case= [{ORTH:contraction},{ORTH:"shall"}]
                nlp.tokenizer.add_special_case(contraction+"'ll",will_case)
                nlp.tokenizer.add_special_case(contraction+"'ll",shall_case)
               
                # there's 
                is_case = [{ORTH:contraction},{ORTH:"is"}]
                has_case = [{ORTH:contraction},{ORTH:"has"}]
                nlp.tokenizer.add_special_case(contraction+"'s",is_case)
                nlp.tokenizer.add_special_case(contraction+"'s",has_case)
                

            elif re.match('(t|T)(hey)',contraction):
                # they'd
                had_case=[{ORTH:contraction},{ORTH:"had"}]
                would_case=[{ORTH:contraction},{ORTH:"would"}]
                nlp.tokenizer.add_special_case(contraction+"'d",had_case)
                nlp.tokenizer.add_special_case(contraction+"'d",would_case)
            
                # they'll
                will_case= [{ORTH:contraction},{ORTH:"will"}]
                shall_case= [{ORTH:contraction},{ORTH:"shall"}]
                nlp.tokenizer.add_special_case(contraction+"'ll",will_case)
                nlp.tokenizer.add_special_case(contraction+"'ll",shall_case)
               
                # they've
                have_case = [{ORTH:contraction},{ORTH:"have"}]
                nlp.tokenizer.add_special_case(contraction+"'ve",have_case)
               
                # they're
                are_case = [{ORTH:contraction},{ORTH:"are"}]
                nlp.tokenizer.add_special_case(contraction+"'re",are_case)


            elif re.match('(w|W)(ere)',contraction):
                # weren't
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)
            

            elif re.match('(w|W)(e)',contraction):
                # we'd
                had_case=[{ORTH:contraction},{ORTH:"had"}]
                would_case=[{ORTH:contraction},{ORTH:"would"}]
                nlp.tokenizer.add_special_case(contraction+"'d",had_case)
                nlp.tokenizer.add_special_case(contraction+"'d",would_case)
            
                #  we're
                are_case = [{ORTH:contraction},{ORTH:"are"}]
                nlp.tokenizer.add_special_case(contraction+"'re",are_case)

                #  we've
                have_case = [{ORTH:contraction},{ORTH:"have"}]
                nlp.tokenizer.add_special_case(contraction+"'ve",have_case)
               
            
            elif re.match('(w|W)(ho)',contraction):
                # who'd
                had_case=[{ORTH:contraction},{ORTH:"had"}]
                would_case=[{ORTH:contraction},{ORTH:"would"}]
                nlp.tokenizer.add_special_case(contraction+"'d",had_case)
                nlp.tokenizer.add_special_case(contraction+"'d",would_case)
            
                # who're
                are_case = [{ORTH:contraction},{ORTH:"are"}]
                nlp.tokenizer.add_special_case(contraction+"'re",are_case)

                # who've
                have_case = [{ORTH:contraction},{ORTH:"have"}]
                nlp.tokenizer.add_special_case(contraction+"'ve",have_case)
               
                
                # who's
                is_case = [{ORTH:contraction},{ORTH:"is"}]
                has_case = [{ORTH:contraction},{ORTH:"has"}]
                nlp.tokenizer.add_special_case(contraction+"'s",is_case)
                nlp.tokenizer.add_special_case(contraction+"'s",has_case)
                

                # who'll
                will_case= [{ORTH:contraction},{ORTH:"will"}]
                shall_case= [{ORTH:contraction},{ORTH:"shall"}]
                nlp.tokenizer.add_special_case(contraction+"'ll",will_case)
                nlp.tokenizer.add_special_case(contraction+"'ll",shall_case)

            elif re.match('(w|W)(hat)',contraction):
                # what're
                are_case = [{ORTH:contraction},{ORTH:"are"}]
                nlp.tokenizer.add_special_case(contraction+"'re",are_case)

                # what've
                have_case = [{ORTH:contraction},{ORTH:"have"}]
                nlp.tokenizer.add_special_case(contraction+"'ve",have_case)
               
                # what's
                is_case = [{ORTH:contraction},{ORTH:"is"}]
                has_case = [{ORTH:contraction},{ORTH:"has"}]
                nlp.tokenizer.add_special_case(contraction+"'s",is_case)
                nlp.tokenizer.add_special_case(contraction+"'s",has_case)
                
                # what'll
                will_case= [{ORTH:contraction},{ORTH:"will"}]
                shall_case= [{ORTH:contraction},{ORTH:"shall"}]
                nlp.tokenizer.add_special_case(contraction+"'ll",will_case)
                nlp.tokenizer.add_special_case(contraction+"'ll",shall_case)
            
            elif re.match('(w|W)(here)',contraction):
                # where're
                are_case = [{ORTH:contraction},{ORTH:"are"}]
                nlp.tokenizer.add_special_case(contraction+"'re",are_case)

                # where've
                have_case = [{ORTH:contraction},{ORTH:"have"}]
                nlp.tokenizer.add_special_case(contraction+"'ve",have_case)
               

            elif re.match('(w|W)(ould)',contraction):
                # wouldn't
                not_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction+"n't",not_case)

            
            elif re.match('(w|W)(ill)',contraction):
                # won't
                willnot_case=[{ORTH:contraction},{ORTH:"not"}]
                nlp.tokenizer.add_special_case(contraction.strip('ill')+"on't",willnot_case)
            
            elif re.match('(y|Y)(ou)',contraction):

                # you'll
                will_case= [{ORTH:contraction},{ORTH:"will"}]
                shall_case= [{ORTH:contraction},{ORTH:"shall"}]
                nlp.tokenizer.add_special_case(contraction+"'ll",will_case)
                nlp.tokenizer.add_special_case(contraction+"'ll",shall_case)

                # you're
                are_case = [{ORTH:contraction},{ORTH:"are"}]
                nlp.tokenizer.add_special_case(contraction+"'re",are_case)

                # you've
                have_case = [{ORTH:contraction},{ORTH:"have"}]
                nlp.tokenizer.add_special_case(contraction+"'ve",have_case)
               
                # you'd
                had_case=[{ORTH:contraction},{ORTH:"had"}]
                would_case=[{ORTH:contraction},{ORTH:"would"}]
                nlp.tokenizer.add_special_case(contraction+"'d",had_case)
                nlp.tokenizer.add_special_case(contraction+"'d",would_case)
            



def extraction(doc,span) -> Doc:
    # checking the word from the merge doc if it is not in the span word
    real_data = [words for words in doc if words.text not in span]
    # print(span)
    print(real_data)
    spaces = []
    for word in real_data:
        # print(word)
        if word.whitespace_:
            spaces.append(True)

        # still checking the  doc we merge , if nbor text is equal to te span word
        elif (word.i+1) < len(doc) and word.nbor(1).text in span:
            #if the alarming word separate two words, add a space.
            spaces.append(True)

        else:
            spaces.append(False)
    # return new doc 
    return  Doc(doc.vocab,words=[word.text for word in real_data],spaces=spaces)



def clean(doc: Doc) -> Doc: 
    # print(doc.text)
    notify_pattern = R'@(\w+|\W+)[:]?'
    hashtags_pattern =R'#\w*[a-zA-Z]+\w*'
    retweet_pattern =R'(RT)+[:]?'
    link_pattern = R'''(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))'''
    pattern = f'{notify_pattern}|{hashtags_pattern}|{retweet_pattern}|{link_pattern}'
    
    # merge all span patterns , so as to combine each of them 
    with doc.retokenize() as retokenizer:
        for match in re.finditer(pattern,doc.text):
            start,end = match.span()
            print(doc.char_span(start,end))
            if doc.char_span(start,end) !=None:
                # print(retokenizer.merge(doc.char_span(start,end)))
                retokenizer.merge(doc.char_span(start,end))
            else: 
                pass
    

    # After combining the words :::: Extract all match words , so as to remove them 
    return extraction(doc,span= [match.group() for match in re.finditer(pattern,doc.text)])
    
    #  spans = []
    # for match in re.finditer(pattern,doc.text):
    #     start,end = match.span()
    #     # print(start,end)

    #     if len(doc[start:end]) !=0:

    #         if (doc.char_span(start,end)==None):
    #             # perform / skip
    #             pass
    #         else:
    #             print(doc.char_span(start,end).text)
    #             if doc.char_span(start,end).text !=None:

    #                 spans.append(doc.char_span(start,end).text)
    #             # print(span)
    #             else: 
    #                 pass


       
        
   
# for i in ["i'm","could","Could","they","They"]:
#     if re.match('(c|C|)(ould)',i):
       
#         print(i)
#     elif re.match("(t|T)(hey)",i):
#         print(i)
#     else:
#         print(i)
