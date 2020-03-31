from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        path = self.path

        message = file_reader(path)

        self.wfile.write(bytes(message, "utf8"))
        return


def file_reader(path):
    if path == "/":
        path = "/index"
        
    try:
        file = open("pages" + path + ".html", 'r')
    except FileNotFoundError:
        file = open("pages.404.html", 'r')
    message = file.read()
    file.close()
    return message


server = HTTPServer(('127.0.0.1', 8081), MyHandler)
server.serve_forever()
