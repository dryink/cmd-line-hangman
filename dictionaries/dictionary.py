# create an empty dictionary
new_dict = {}

# create a dictionary by adding values to it
new_dict['key1'] = 'value1'
new_dict['key2'] = 'value2'
new_dict[3] = 'value3'

# or create/populate at once
other_dict = {'key1': 'value1', 'key2': 'value2', 3: 'value3'}

# inspect it a bit
print "Dictionary:", new_dict
print "Keys:", new_dict.keys()
print "Values:", new_dict.values()

# loop by key
for k in new_dict:
    print "Value:", new_dict[k]

# get key & item in one swoop
for key, val in new_dict.items():
    print "Key", key, "Value", val