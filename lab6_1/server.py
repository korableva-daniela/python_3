from http.server import HTTPServer, CGIHTTPRequestHandler
port = 8080
httpd = HTTPServer(("", port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port)+" http://localhost:8080/login.html")
httpd.serve_forever()