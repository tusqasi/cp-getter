from http.server import HTTPServer, BaseHTTPRequestHandler
import json

global question


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-length", 0))
        data = self.rfile.read(length).decode()
        global question
        
        question = json.loads(data)
        print(question)
        self.send_response(200)
        self.end_headers()
        self.flush_headers()
        self.server.server_close()
        print("here")

def main():
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
    print("close")
    return question


if __name__ == "__main__":
    print(main())
