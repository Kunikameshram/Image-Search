import random
import os
import sys
print(sys.path)
import grpc
from concurrent import futures
import Image_search__pb2
import Image_search__pb2_grpc


class ImageSearchServicer(Image_search__pb2_grpc.ImageSearchServicer):
    def __init__(self, image_folder):
        self.image_folder = image_folder

    def SearchImage(self, request, context):
        keyword = request.keyword
        images = [f for f in os.listdir(self.image_folder) if keyword in f]
        if images:
            image_file = random.choice(images)
            with open(os.path.join(self.image_folder, image_file), "rb") as f:
                image_data = f.read()
            return Image_search__pb2.ImageResponse(image_data=image_data)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No image found for the given keyword")
            return Image_search__pb2.ImageResponse()

def serve(image_folder):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Image_search__pb2_grpc.add_ImageSearchServicer_to_server(
        ImageSearchServicer(image_folder), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server listening on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <image_folder> <port>")
        sys.exit(1)
        
    image_folder = sys.argv[1]
    print("image_folder:" + image_folder)
    # port = int(sys.argv[2])
    serve(image_folder)