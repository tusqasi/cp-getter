import sys
import get_question
import put_io
import make_template

TOKEN = sys.argv[1]
question = get_question.get_question(TOKEN)
if put_io.put_io(question['name'], question['io']): # is true when no existsting question is found
    make_template.make_template(question['URL'])
print( question['name'])