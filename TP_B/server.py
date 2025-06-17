"""HTTP server"""

from socketserver import TCPServer, StreamRequestHandler
from datetime import datetime

class Handler(StreamRequestHandler):
    def handle(self):
        first_line = self.rfile.readline().decode().strip()
        response = ''

        try:
            method, path, version = first_line.split()
        
            code = '200 OK'

            if path == '/':
                content = 'Hello World!'
            elif path == '/date':
                content = f"Date du jour: {datetime.now().strftime('%A %d %B %Y, %H:%M:%S')}\n"
            else:
                content = '404 Not Found'
                code = '404 Not Found'

            response = f"""{version} {code}
Content-Type: text/plain
Content-Length: {len(content)}
Connection: close
            
{content}"""
        except ValueError:
            response = """HTTP/1.1 400 Bad Request
Content-Type: text/plain
Content-Length: 12
Connection: close
        
400 Bad request"""
        finally:
            self.wfile.write(response.encode())

        

if __name__ == '__main__':
    try:
        with TCPServer(('localhost', 8080), Handler) as server:
            server.serve_forever()
    except (KeyboardInterrupt, OSError):
        print('')
    