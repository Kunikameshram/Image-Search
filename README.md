# Image Search Service

This project implements a gRPC-based image search service in Python. The server returns an image file from a directory that matches a given keyword. The client requests an image by keyword and saves the result.

## Project Structure

- `Server/ImageServer.py`: gRPC server implementation.
- `Client/ImageClient.py`: gRPC client implementation.
- `protos/Image_search_.proto`: Protocol Buffers definition for the gRPC service.
- `images/`: Directory containing sample images (e.g., `cat.jpg`, `dog.jpg`).
- `requirements.txt`: Python dependencies.
- `Dockerfile.server`: Dockerfile for the server.
- `Dockerfile.client`: Dockerfile for the client.

## Prerequisites

- Python 3.9+
- `pip`
- `grpcio-tools` (installed via `requirements.txt`)
- Docker (optional, for containerized usage)

## Setup

1. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

2. **Generate gRPC code from proto file:**

   ```sh
   python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/Image_search_.proto
   ```

   This will generate `image_search__pb2.py` and `image_search__pb2_grpc.py` in your project root.

3. **Prepare images:**

   Place images (e.g., `cat.jpg`, `dog.jpg`) in the `images/` directory.

## Running Locally

### Start the Server

```sh
python Server/ImageServer.py images/
```

### Run the Client

```sh
python Client/ImageClient.py
```

Enter a keyword (e.g., `cat`) when prompted. If an image matching the keyword exists, it will be saved as `<keyword>.jpg` in the current directory.

## Using Docker

### Build and Run the Server

```sh
docker build -f Dockerfile.server -t image-search-server .
docker run -v $(pwd)/images:/app/images -p 50051:50051 image-search-server
```

### Build and Run the Client

```sh
docker build -f Dockerfile.client -t image-search-client .
docker run -it --network host image-search-client
```

## Proto Service Definition

See [`protos/Image_search_.proto`](protos/Image_search_.proto):

- `rpc SearchImage (KeywordRequest) returns (ImageResponse)`

## Notes

- The server searches for images whose filenames contain the keyword.
- If no image is found, the server returns a NOT_FOUND error.
- The client saves the received image as `<keyword>.jpg`.

