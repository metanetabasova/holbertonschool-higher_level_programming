#!/usr/bin/python3
import http.server
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    '''Sade HTTP server ucun request handler sinfi.'''

    def do_GET(self):
        '''GET sorgularini idare edir'''

        # sade metn cavabi
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # JSON melumati
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            sample_data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(sample_data).encode('utf-8'))

        # status yoxlanisi
        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        # 404 xetasi
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def run_server():
    '''serveri 8000 portunda basladir.'''
    port = 8000
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server {port} portunda isleyir...")
    httpd.server_forever()

if __name__ == '__main__':
    run_server()
