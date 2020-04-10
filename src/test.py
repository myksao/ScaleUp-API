
# Using @staticmethod or classmethod  i.e decorator

class Meta:

    @staticmethod
    def db(name):
        return name
class Dob:

    @staticmethod
    def db(name):
        return name


class DB(Meta,Dob):
   
   @staticmethod
   def res(name):
        # print(Dob.db(name))
        return Meta.db(name)


result = DB.res(name ='Whats good')
print(result)




# Second example  using self

class Test:

    def meta(self):
        print(self + ' '+ 'Hi')


class Group(Test):
    
    def answer(self):
        return Test.meta(self)


result = Group.answer('hey')


# global 
sname = ''
class Ever:

    def __init__(self, name):
        global sname
        sname = name 

    @staticmethod
    def nice():
        print(sname)


Ever(name ='Hey').nice()


def myfunc(a):
  return a

x = list(map(myfunc, ('apple', 'banana', 'cherry')))
# or
# for ch in map(myfunc,['hi',hello]):
print(x)


# 

import base64

message = "Python is fun"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)

# Instance method __init__ - special params i.e self
# class method @classmethod - special parameter i.e cls
# static method @staticmethod - no special or required params

class Dev:

    def __init__(self):
        self.arr = ''

    def hey(self):
        self.arr = []
    
    def addarr(self,value):
        self.arr = value
        return self.arr

    

obj1 = Dev()
print(obj1.addarr(value = 10))
print(obj1.arr)


class Stat:

    @staticmethod
    def statio(value):
        return value


print(Stat.statio(value='20'))


# Asyncio - makes a function to hold on before proceeding
# import asyncio
# def hey(value):
#     result = value**100
#     print(result)
#     return value

    
# async def funcname(value):
#     await asyncio.sleep(10,result= hey(value=int(50)))
#     print(value)

# asyncio.run(funcname(value= 'Hi'))



def yieldgen():
    for i in range(0,10,2):
        yield i
        print(i)


# for x in yieldgen():
#     print(x)



checkbill =''
sector  = 2

if sector ==0:
    checkbill = ''
    checkbill = 'Health'

elif sector == 1:
    checkbill = 'Housing'
    print(checkbill)

elif sector == 2:
    checkbill = 'Secure'
    print (checkbill)

# check if empty
if len(checkbill)!=0:  
    print('Uhn')
# check if empty
elif not checkbill:
    print('Yay')
# check if not empty
else:
    print('Awwn')


print(checkbill)

# async def hi():
#    r = await 10**66
#    return r

# result = hi()

# print(result)

meta = dict()

meta['collection'] = 'health'

print(meta)

from src.models import Opinion


class A:

    def __init__(self,conn):
        self._conn = conn
        print(self._conn)








async def testhey():
    r = await Opinion.opinions(sector=1)
    return r

testhey()
