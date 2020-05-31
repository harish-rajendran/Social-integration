

import os
import json

#os.chdir(r"C:\Users\Admin\Documents\py2020")
#print("WARNING: Directory changed")
details = {"name":"riha","work":{"first": "TCS","second":"netflix"},"city":{"first":{"India":{"one":"Mumbai","two":"Chennai"}}}}
#print(type(details))
dictionary = json.dumps(details,indent = 4)
with open('wsample.json','w+') as outfile:
    json.dump(dictionary,outfile)
outfile.close()
print("done writing")

with open ('wsample.json','r+') as infile:
    cred = json.load(infile)
infile.close()
#print(cred)

value = json.loads(cred)
print(value["city"]["first"]["India"]["one"])

'''parsed = json.loads(details)
print(type(parsed))
print(parsed["city"])'''




