# fetch data from any source of dataset either online or user importing dataset themselves
# then forward it to raw folder
import csv
import  re
import requests
from pathlib import Path
import  json


# with open('catchme/data/raw/files.txt','wt') as files:
#     files.write('Hi')   
class Preparation:
        # *args => tuples
        # **kwargs => dict
    def __init__(self,urls,custom_sentiment:str):
            self.urls = urls
            self.custom_sentiment = custom_sentiment
            
        

    async def new_imported_data(self):
        
        for url in self.urls:
            print(url)
            if re.match('http[s]?://[w+]?.+', url)!=None:   
                if re.match('^[\w\W]+[.csv]+$',url)!=None:
                    csv_row=[]
                    request = requests.get(url, stream=True)
                    if 'Content-Disposition' in request.headers.keys():
                        fileheader = request.headers['content-disposition']
                        filename = re.findall('filename(.+)',fileheader)[0]
                        with open(f'catchme/data/raw/{filename}.json','wt',newline='') as filedata:
                            reader = csv.DictReader(request.content)
                            field = reader.fieldnames
                            for row in reader:
                                csv_row.extend([{field[i]:row[field[i]] for i in range(len(field))}])
                            filedata.write(json.dumps(csv_row, indent=4, sort_keys=False,separators=(',',':')))
                    else:
                        filename= url.split('/')[-1]
                        with open(f'catchme/data/raw/{filename}.json','wt') as filedata:
                            reader = csv.DictReader(request.content)
                            field = reader.fieldnames
                            for row in reader:
                                csv_row.extend([{field[i]:row[field[i]] for i in range(len(field))}])
                            filedata.write(json.dumps(csv_row, indent=4, sort_keys=False,separators=(',',':')))
                      

                elif  re.match('^[\w\W]+[.txt]+$',url) !=None:
                    rawdata=[]
                    request = requests.get(url, stream=True)
                    if 'Content-Disposition' in request.headers.keys():
                        fileheader = request.headers['content-disposition']
                        filename = re.findall('filename(.+)',fileheader)[0]
                        with open(f'catchme/data/raw/{filename}.json','wt') as filedata:
                            for row in request.iter_lines():

                                '''we can use re.search('(0|Negative|negative)$',row).group() to
                                get the match item but due to the noisy way data are stored , we decide for now
                                to hardcode the sentiment value after checking the match that matches the end value 
                                '''
                                if self.custom_sentiment == None:
                                    if re.search('(0|Negative|negative)$',row)!=None:
                                        rawdata.extend([{'sentiment':'Negative','text':row.strip('0 \t0\n \t1\n')}])
                                    elif re.search('(1|Positive|positive)$',row)!=None:
                                        rawdata.extend([{'sentiment':'Positive','text':row.strip('1 \t0\n \t1\n')}]) 
                                    elif re.search('(0.5|Neutral|neutral)$',row)!=None:
                                        rawdata.extend([{'sentiment':'Neutral','text':row.strip('0.5 \t0\n \t1\n')}]) 
                                else:
                                    if self.custom_sentiment == 'Negative':
                                        rawdata.extend([{'sentiment':'Negative','text':row.strip('0.5 \t0\n \t1\n')}])
                                    elif self.custom_sentiment == 'Positive':
                                        rawdata.extend([{'sentiment':'Positive','text':row.strip('0.5 \t0\n \t1\n')}])
                                    elif self.custom_sentiment == 'Neutral':
                                        rawdata.extend([{'sentiment':'Neutral','text':row.strip('0.5 \t0\n \t1\n')}])
                                 
                        filedata.write(json.dumps(rawdata, indent=4, sort_keys=False,separators=(',',':')))
                         
	
                    else:
                        filename= url.split('/')[-1]
                        with open(f'catchme/data/raw/{filename}.json','wt') as filedata:
                            for row in request.iter_lines():

                                '''we can use re.search('(0|Negative|negative)$',row).group() to
                                get the match item but due to the noisy way data are stored , we decide for now
                                to hardcode the sentiment value after checking the match that matches the end value 
                                '''
                                if self.custom_sentiment == None:
                                    if re.search('(0|Negative|negative)$',row)!=None:
                                        rawdata.extend([{'sentiment':'Negative','text':row.strip('0 \t0\n \t1\n')}])
                                    elif re.search('(1|Positive|positive)$',row)!=None:
                                        rawdata.extend([{'sentiment':'Positive','text':row.strip('1 \t0\n \t1\n')}]) 
                                    elif re.search('(0.5|Neutral|neutral)$',row)!=None:
                                        rawdata.extend([{'sentiment':'Neutral','text':row.strip('0.5 \t0\n \t1\n')}]) 
                                else:
                                    if self.custom_sentiment == 'Negative':
                                        rawdata.extend([{'sentiment':'Negative','text':row.strip('0.5 \t0\n \t1\n')}])
                                    elif self.custom_sentiment == 'Positive':
                                        rawdata.extend([{'sentiment':'Positive','text':row.strip('0.5 \t0\n \t1\n')}])
                                    elif self.custom_sentiment == 'Neutral':
                                        rawdata.extend([{'sentiment':'Neutral','text':row.strip('0.5 \t0\n \t1\n')}])
                                 
                            filedata.write(json.dumps(rawdata, indent=4, sort_keys=False,separators=(',',':')))
                         

            elif re.match('^[\w\W]+[.csv]+$',url):
                filepath =  Path(url).stem
                csv_row=[]
                url = url.lstrip('\u202a')
                with open(url,'r',errors='ignore') as readtxt:
                    with open(f'catchme/data/raw/{filepath}.json','w') as filedata:
                        reader = csv.DictReader(readtxt)
                        field = reader.fieldnames
                        for row in reader:
                            csv_row.extend([{field[i]:row[field[i]] for i in range(len(field))}])
                        # # writer.writerows(readtxt.readlines())
                            filedata.write(json.dumps(csv_row, indent=4, sort_keys=False,separators=(',',':')))
                         
                            
            elif re.match('^[\w\W]+[.txt]+$',url):
                rawdata=[]
                filepath = Path(url).stem
                url = url.lstrip('\u202a')
                with open(url,'r') as readtxt:
                    with open(f'catchme/data/raw/{filepath}.json','w') as filedata:
                        for row in readtxt.readlines():
                            '''we can use re.search('(0|Negative|negative)$',row).group() to
                            get the match item but due to the noisy way data are stored , we decide for now
                            to hardcode the sentiment value after checking the match that matches the end value 
                            '''
                            if self.custom_sentiment == None:

                                if re.search('(0|Negative|negative)$',row)!=None:
                                    rawdata.extend([{'sentiment':'Negative','text':row.strip('0 \t0\n \t1\n')}])
                                elif re.search('(1|Positive|positive)$',row)!=None:
                                    rawdata.extend([{'sentiment':'Positive','text':row.strip('1 \t0\n \t1\n')}]) 
                                elif re.search('(0.5|Neutral|neutral)$',row)!=None:
                                    rawdata.extend([{'sentiment':'Neutral','text':row.strip('0.5 \t0\n \t1\n')}]) 
                            else:
                                if self.custom_sentiment == 'Negative':
                                    rawdata.extend([{'sentiment':'Negative','text':row.strip('\t0\n \t1\n')}])
                                elif self.custom_sentiment == 'Positive':
                                    rawdata.extend([{'sentiment':'Positive','text':row.strip('\t0\n \t1\n')}])
                                elif self.custom_sentiment == 'Neutral':
                                    rawdata.extend([{'sentiment':'Neutral','text':row.strip('\t0\n \t1\n')}])
                                   
                        filedata.write(json.dumps(rawdata, indent=4, sort_keys=False,separators=(',',':')))
                         
	
        
                        
        
      
      





