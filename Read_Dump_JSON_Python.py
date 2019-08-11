# To save data in JSON format 
import json
with open('my_dict.json', 'w') as f:
    json.dump(my_dict, f)
    
# To read data from a JSON file
import json
f = open('my_dict.json')
my_dict = json.load(f)
# when finished, close the file
f.close()

with open('my_dict.json', 'r') as f:
    my_dict = f.read()
