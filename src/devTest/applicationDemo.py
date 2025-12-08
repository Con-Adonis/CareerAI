import os
import time
#from sentence_transformers import SentenceTransformer, util
import re
import json

'''
#configuration and constants
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
similarityScore = 0.85
mockApplication = os.path.abspath("mock_job_app.html")


#embeds and compares strings using above model
def stringComparison(str1, str2):
    print(f"{str1} and {str2}: {util.pytorch_cos_sim(model.encode(str1), model.encode(str2)).item()}")
    return util.pytorch_cos_sim(model.encode(str1), model.encode(str2)).item()
'''

#Application parser, for demo purposes it is more hardcoded
def readApplication():
    pathname = "src/devTest/applicationExample.html"

    #check pathing
    if os.path.exists(pathname):
        app = open(pathname, "r")
    else:
        print("Pathname Error")

    #line by line parsing
    for line in app:
        if "label for" in line:
            print(f"before: {line}")
            #TODO: parse HTML info correctly
            question = filterWording(line.strip())
            stringComparison(question)

def filterWording(line):
    between = False
    question = ""
    for c in line[1:]:
        if c == ">":
            between = True
            continue
        
        if c == "<":
            return question
        
        if between:
            question += c
        
    return("Error extracting question")

def stringComparison(line):
    with open('data/userInfo.json', 'r') as f:
        userData = json.load(f)
    
    print(f"{line}, {userData}")


readApplication()