from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Lists of users and messages
all_pseudos = []
all_messages = []

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write('Bienvenue sur CanaDuck !'.encode())
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        """
        /nick : save a nickname
        Excepted content:
        {'pseudo': '...'}

        /msg : save a message
        Excepted content:
        {'from': '...';
        'message': '...'}
        """
        try:
            if self.path == '/nick':
       
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length)

                data = json.loads(body)
                pseudo = data.get('pseudo', '')

                if len(pseudo) > 4:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain; charset=utf-8')
                    self.end_headers()
                    self.wfile.write('Nickname saved'.encode('utf-8'))
                    all_pseudos.append(pseudo)
                else:
                    raise ValueError
            elif self.path == '/msg':
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length)

                data = json.loads(body)
                author = data.get('from', '')
                message = data.get('message', '')

                if len(author) > 4 and len(message) > 4:
                    self.send_response(201)
                    self.send_header('Content-type', 'text/plain; charset=utf-8')
                    self.end_headers()
                    self.wfile.write('Nickname saved'.encode('utf-8'))
                    all_messages.append((author, message))
                else:
                    raise ValueError
            else:
                self.send_error(404, 'Not Found')
                data = json.loads(body)

        except (json.JSONDecodeError, ValueError):
            self.send_response(400)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write('Invalid date send'.encode())

        

if __name__ == '__main__':
    try:
        server = HTTPServer(('', 8080), Handler)
        print("Server listening on 8080")
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
