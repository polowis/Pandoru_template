import socketserver
import http.server

PORT = 8000
handler = http.server.SimpleHTTPRequestHandler

routes = {}

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        views = routes.get(self.path)
        self.path = view
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
    def address_string(self):
        return self.client_address[0]

    def log_message(self):
        ex = {
            'request': self.requestline,
            'server_time': self.log_date_time_string()
        }


def run():

    handler_object = RequestHandler

    server = socketserver.TCPServer(("", PORT), handler_object)

    # Star the server
    server.serve_forever()
