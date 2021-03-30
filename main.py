#!/home/tusqasi/Documents/wars/py/cp_problem_getter/.wars/bin/python3
import sys
import get_question
import put_io
import make_template
def get_token():
    try:
        return sys.argv[1]
    except IndexError:
        print("No URL specified\
             \nSpecify URL like:\
             \npython main.py <URL>\
             \n\n Exiting")
        exit()

TOKEN = get_token()
question = get_question.get_question(TOKEN)
if put_io.put_io(question["name"], question["io"]):
    make_template.make_template(question["URL"])
print(question["name"])
