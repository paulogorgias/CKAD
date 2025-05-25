from http.server import BaseHTTPRequestHandler, HTTPServer
import time

start_time = time.time()
unhealthy = False  # Flag para simular falha manual

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global unhealthy
        uptime = time.time() - start_time

        if self.path == "/health":
            if unhealthy:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Liveness failed: manually triggered.")
            else:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Liveness OK")

        elif self.path == "/ready":
            if uptime < 15:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Not ready yet.")
            else:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Ready")

        elif self.path == "/startunhealth":
            unhealthy = True
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Liveness failure activated.")

        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"Hello from fake app. Uptime: {int(uptime)}s".encode())

HTTPServer(("", 8000), Handler).serve_forever()
