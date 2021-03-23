import sys

TOKEN = sys.argv[1]

question = get_question(TOKEN)
put_tcs(question['name'], question['io'])
make_template(question['URL'])
