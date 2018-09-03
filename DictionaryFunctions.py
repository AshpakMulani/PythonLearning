#stores value in {key:value , key1:value1} format. Key always should be a string
# In dictionary objects are retrieved by key names not using index. Means objects does not have indexed order
# hence objects in dictionary can not be sorted.
# In lists on other hand,objects are retrieved by index. Means objects have indexed order
# hence objects in list can be sorted, indexed or sliced.

my_dict = {'key1':'value1', 'key2':28}
print(my_dict)
print(my_dict['key2'])  # getting value for key2

#add new key pair
my_dict['key2']  = 'hello' #replacing existing key value
my_dict['key3'] = 'value3'
my_dict['key4'] = [1,2,3,4] # embading list at key4
print(my_dict)

#get list of all keys in dict
print(my_dict.keys())
#get list od all values
print(my_dict.values())
#get list of items from dict. It returns "tuples"
print(my_dict.items())

#nasted dict
my_dict_nested= {'key1':'value1', 'nested_key1':{'key1':'value1'}, 'key2':'value2'}
print(my_dict_nested)  # nested dictionary should have a key in parent dictionary
print(my_dict_nested['nested_key1']) #accessing complete nested dictionary
print(my_dict_nested['nested_key1']['key1']) #accessing keys in nested dictionary

#we can embade other data types in dictionary like list
#pythin supports embading any data structure in other data structure.
my_hybd_dict={'key1':'value1',
              'key2':[      #embading list containing dictionaries within
                        {'nkey1':'nval1','nkey2':'nval2'},
                        {'nkey3':'nval3','nkey4':'nval4'},
                    ],
              'key3':'val3'
              }
print(my_hybd_dict)
print(my_hybd_dict['key2'][1]['nkey4']) #getting last value from embaded list's second dictionary
                                        # Key2 = accessing key2 which will return list
                                        # then from list access item from index1, which is second list
                                        # then from second dict access nkey4 value.





#########################################################################33
st = 'Print every word in this sentence that has an even number of letters'
my_dict={}
my_list=st.split()
for x in my_list:
    if len(x)%2==0:
        my_dict[x] = 'even!'
    else:
        my_dict[x] = 'odd!'
print(my_dict)