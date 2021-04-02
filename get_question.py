from http.server import HTTPServer, BaseHTTPRequestHandler
import json

question: dict


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-length", 0))
        data = self.rfile.read(length).decode()
        question = json.loads(data)
        httpd.shutdown()
def main():
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
    return question

if __name__ == "__main__":
    main()