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


def main():
    question = get_question_http.main()
    if put_io.put_io(question["name"], question["tests"]):
        make_template.make_template(question["url"])
    print(question["name"])


def testing():
    get_config()


# testing()
if __name__ == "__main__":
    main()
