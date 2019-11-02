import json
import os
import signal
import sys
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length'))
        body = self.rfile.read(content_length).decode('utf-8')
        message = json.loads(body)

        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(message['content'])

        self._set_headers(200)
        self.wfile.write(bytes(json.dumps(vs), "utf-8"))

class Server():
    def __init__(self, handler):
        self.handler = handler

    def start(self, port):
        self.http_server = HTTPServer(("", port), self.handler)

        print("listening on port:", port)
        self.server_thread = threading.Thread(target=self.http_server.serve_forever)
        self.server_thread.start()

    def stop(self, signal, frame):
        print("stopping")
        self.http_server.shutdown()
        self.server_thread.join()
        print("stopped")

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))

    server = Server(RequestHandler)

    signal.signal(signal.SIGINT, server.stop)
    signal.signal(signal.SIGTERM, server.stop)

    server.start(port)