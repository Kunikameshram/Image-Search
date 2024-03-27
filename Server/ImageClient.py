import os
import sys
import grpc
import Image_search__pb2
import Image_search__pb2_grpc
import os

def search_image(keyword, host="172.17.0.2", port=50051):
    channel = grpc.insecure_channel(f"{host}:{port}")
    stub = Image_search__pb2_grpc.ImageSearchStub(channel)
    response = stub.SearchImage(Image_search__pb2.KeywordRequest(keyword = keyword))
    return response

if __name__ == "__main__":

    keyword = input("Enter keyword to search: ")
    response = search_image(keyword)
    
    # directory where image will be saved
    save_directory = "/app/ClientImagesReceived/"
    
    # Create the directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)
    
    # Save the image to the specified directory
    image_filename = f"{keyword}.jpg"
    image_path = os.path.join(save_directory, image_filename)
    with open(image_path, "wb") as f:
        f.write(response.image_data)
    
    print(f"Image saved as {image_path}")
