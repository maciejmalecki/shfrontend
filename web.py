#!/usr/bin/env python
"""
Very simple HTTP server in python.

Usage::
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import logging, logging.handlers

LOG_FILE_NAME='log/web.log'

logging.basicConfig(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh = logging.handlers.TimedRotatingFileHandler(LOG_FILE_NAME, when='midnight', backupCount=5)
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger = logging.getLogger('shweb')
logger.propagate = False
logger.addHandler(fh)

msg = 'Empty'

class S(BaseHTTPRequestHandler):


    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>" + msg + "</h1><script>window.setTimeout(()=>window.location.reload(),10000);</script></body></html>")

    def do_POST(self):
	global msg
	content_len = int(self.headers.getheader('content-length', 0))
        msg = self.rfile.read(content_len)
	logger.debug(msg)
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")

    def log_message(self, format, *args):
        return

        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logger.info('Starting SmartHome httpd on port %d', port)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

