import random
import os
import grpc
from concurrent import futures
import sqlite3
import io
import Image_search__pb2
import Image_search__pb2_grpc
from database import DatabaseManager


class ImageSearchServicer(Image_search__pb2_grpc.ImageSearchServicer):
    def __init__(self):
        self.image_folder = "/app/images"  # Set the image folder path here
        self.db_file = "image_metadata.db"  # Set the database file name here
       
        self.db_manager = DatabaseManager(self.db_file)
    

    def get_matching_images(self, keyword):
        filenames = self.db_manager.search_image(keyword)
        print(f"Matching filenames for keyword '{keyword}': {filenames}")  # Debugging statement
        return [os.path.join(self.image_folder, filename) for filename in filenames]

    def get_random_image(self, keyword):
        matching_images = self.get_matching_images(keyword)
        if matching_images:
            image_file = random.choice(matching_images)
            print(f"Selected image file: {image_file}")  # Debugging statement
            if os.path.exists(image_file):  # Check if file exists
                if os.access(image_file, os.R_OK):  # Check if file is readable
                    with open(image_file, "rb") as f:
                        image_data = f.read()
                    return image_data
                else:
                    print(f"File '{image_file}' is not readable.")  # Debugging statement
            else:
                print(f"File '{image_file}' does not exist.")  # Debugging statement
                return None  # Return None if file doesn't exist
        else:
            return None

    def SearchImage(self, request, context):
        keyword = request.keyword
        image_data = self.get_random_image(keyword)
        if image_data:
            return Image_search__pb2.ImageResponse(image_data=image_data)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No image found for the given keyword")
            return Image_search__pb2.ImageResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Image_search__pb2_grpc.add_ImageSearchServicer_to_server(
        ImageSearchServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server listening on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()