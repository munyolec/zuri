#register
#login

#Dictionary

aSampleList=[1,2,3,4,5]

#methodOne

dictionaryOne={
    'key1':'value1',
    'key2':'value2',
    'key3':'value3'
}

#methodtwo
dictionaryTwo={}
dictionaryTwo['key4']= 'value4'
dictionaryTwo['key5']= 'value5'
dictionaryTwo['key6']= 'value6'
dictionaryTwo['key7']= 'value7'

# print(dictionaryOne)

# dictionaryTwo.pop('key7')
# print(dictionaryTwo)

#Dictionary loop

for key, value in dictionaryTwo.items():
    print ("I have "+key +" thats related to "+value)
