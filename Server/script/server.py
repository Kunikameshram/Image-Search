import http.server
import json
import grpc
import Image_search__pb2
import Image_search__pb2_grpc

# Initialize gRPC channel
channel = grpc.insecure_channel('50051:50051')
stub = Image_search__pb2_grpc.ImageSearchStub(channel)

class MyHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        keyword = json.loads(post_data.decode('utf-8')).get('keyword')
        image_data = self.search_image(keyword)
        self.send_response(200)
        self.send_header('Content-type', 'application/octet-stream')
        self.end_headers()
        self.wfile.write(image_data)

    # def do_GET(self):
    #     self.send_response(200)
    #     self.send_header('Content-type', 'text/html')
    #     self.end_headers()
    #     self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")

    def search_image(self, keyword):
        response = stub.SearchImage(Image_search__pb2.KeywordRequest(keyword=keyword))
        return response.image_data

def run(server_class=http.server.HTTPServer, handler_class=MyHttpRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting http server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
