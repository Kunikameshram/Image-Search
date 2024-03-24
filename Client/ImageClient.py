import grpc
import tempfile
import image_search__pb2
import image_search__pb2_grpc
import requests
import os

def search_image(keyword, host="localhost", port=50051):
    channel = grpc.insecure_channel(f"{host}:{port}")
    stub = image_search__pb2_grpc.ImageSearchStub(channel)
    response = stub.SearchImage(image_search__pb2.KeywordRequest(keyword=keyword))
    return response

if __name__ == "__main__":
    keyword = input("Enter keyword to search: ")
    response = search_image(keyword)
    
    # Create a temporary file to store the image data
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_image:
        temp_image.write(response.image_data)
        temp_image_path = temp_image.name
    
    # Save the image to the current directory
    image_filename = f"{keyword}.jpg"
    with open(image_filename, "wb") as f:
        f.write(response.image_data)
    
    print(f"Image saved as {image_filename}")
