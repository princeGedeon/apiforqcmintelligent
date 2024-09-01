# FastAPI + Pytorch GPU Docker Setup

This project sets up a FastAPI application with Pytorch using GPU support via Docker and Conda.

## Prerequisites

- Docker installed on your machine.
- NVIDIA drivers and CUDA toolkit installed for GPU support.

## Setup

1. Clone this repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Build the Docker image:
    ```bash
    docker-compose build
    ```

3. Start the application:
    ```bash
    docker-compose up
    ```

4. The API will be accessible at `http://localhost:8000`.

## API Endpoints

- **POST** `/generate-qcm`: Generates a QCM based on the provided lyrics.

### Example Request:

```json
{
  "lyrics": "Some lyrics here",
  "default_format": false
}
"# apiforqcmintelligent" 
