# fetch data from any source of dataset either online or user importing dataset themselves
# then forward it to raw folder
import  re
import requests
import  os


def new_imported_data(id,*urls):
    if id==0:
        for url in urls:
            request = requests.get(urls, stream=True)
            fileheader = request.headers['content-disposition']
            filename = re.findall('filename(.+)',fileheader)[0]
            with open('data/raw/{filename}','wb') as filedata:
                filedata.write(request.content)
                filedata.close()
    elif id ==1:
        for devicetxt in urls:
            filepath =  os.path.basename(devicetxt)
            with open(devicetxt,'rb') as readtxt:
                with open('data/raw/{filepath}','wb') as filedata:
                    filedata.write(readtxt.read())
                    readtxt.close()
                    filedata.close()
    
    
        
if __name__ == "__main__":
    new_imported_data(1,)
    

