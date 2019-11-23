import json
import ast
with open('bulkV2.json') as file: 
    jsondata = file.read()
    data = ast.literal_eval()