from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('127.0.0.1', 8531)
    httpd = server_class(server_address, handler_class)
    print(f"Server starting on http://127.0.0.1:8531")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
