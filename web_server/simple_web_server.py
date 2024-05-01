import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.join(os.getcwd(), 'public_html'), **kwargs)

def run(server_class=HTTPServer, handler_class=CustomHandler):
    server_address = ('', 8000)  # Server on localhost, port 8000
    httpd = server_class(server_address, handler_class)
    print("Starting simple web server on localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

