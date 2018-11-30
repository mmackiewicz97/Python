#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
#HTTPRequestHandler class
class testHTTPSever_RequestHandler(BaseHTTPRequestHandler):
    #GET
    def do_GET(self):
        #Send response status code
        self.send_response(200)

        #Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        imsi = query_components["X"]

        #Send message back to client
        message = "Hello world!"
        #Write content as utf-8 data
        foo = "<h1> hello: {} </h1>".format(imsi)
        self.wfile.write(bytes(foo, "utf8"))
        return
    def do_POST(self):
        #Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) #<-- Gets the size
        #data
        post_data = self.rfile.read(content_length) #<-- Gets the data itself
        self.send_header('Content-type', 'tect/html')
        self.wfile.write(bytes(str(post_data), "utf8"))

    def run(self):
        print('starting server...')

        #Server settings
        #Choose port 8080, for port 80, which is normally used for a http server
        #you d root access
        server_address = ('127.0.0.1', 8081)
        httpd = HTTPServer(server_address, testHTTPSever_RequestHandler)
        print('running server...')
        httpd.serve_forever()

testHTTPSever_RequestHandler.run(0)

#python3 -m http.server -cpi 80
#http://127.0.0.1:8081/?X=2