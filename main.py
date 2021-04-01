#!/home/tusqasi/Documents/wars/py/cp_problem_getter/.wars/bin/python3
import sys
import get_question
import put_io
import make_template
import json

def GetJsonFromFile(filePath):
    contents = ""
    fh = open(filePath)
    for line in fh:
        cleanedLine = line.split("//", 1)[0]
        if len(cleanedLine) > 0 and line.endswith("\n") and "\n" not in cleanedLine:
            cleanedLine += "\n"
        contents += cleanedLine
    fh.close
    while "/*" in contents:
        preComment, postComment = contents.split("/*", 1)
        contents = preComment + postComment.split("*/", 1)[1]
    return contents

def get_config():
    try:
        
        config = GetJsonFromFile("~/.config/cp-getter.json")
        print(config)
    except FileNotFoundError:
        print("No config file found")
        exit()
        
def get_token():
    try:
        return sys.argv[1]
    except IndexError:
        print(
            "No URL specified\
           \nSpecify URL like:\
           \npython main.py <URL>\n\
           \nExiting"
        )
        exit()

def main():
    TOKEN = get_token()
    question = get_question.get_question(TOKEN)
    if put_io.put_io(question["name"], question["io"]):
        make_template.make_template(question["URL"])
    print(question["name"])
   
    
def testing():
    get_config()

testing()