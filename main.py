import sys
import get_question
import put_io
import make_template

TOKEN = sys.argv[1]
print(TOKEN)
question = get_question.get_question(TOKEN)
put_io.put_io(question['name'], question['io'])
make_template.make_template(question['URL'])
