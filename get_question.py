from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import threading
from queue import Queue

global question

question = None
class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-length", 0))
        data = self.rfile.read(length).decode()
        global question
        question = json.loads(data)
        self.send_response(200)
        self.end_headers()
        self.flush_headers()

def not_main(s):
    while True:
        if (type(question) == dict):
            s.shutdown()
            return
def main():
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, MessageHandler)

    server = threading.Thread(target=httpd.serve_forever)
    hmm = threading.Thread(target=not_main, args=(httpd,) )
    server.start()
    hmm.start()
    server.join()
    return question
if __name__ == "__main__":
    main()