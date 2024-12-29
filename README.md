# Docker Compose Test

This repository contains a sample project to demonstrate the usage of Docker Compose with a Python application.

## Features

- Multi-container Docker application using Docker Compose.
- Python application setup with dependencies.
- Sample configuration for development and testing.

## Prerequisites

- Docker installed on your machine. You can download it from [here](https://www.docker.com/products/docker-desktop).
- Docker Compose installed. It usually comes with Docker Desktop installation.

## Getting Started

1. **Clone the repository:**
    ```sh
    git clone https://github.com/SahanWeerasiri/docker-compose-test.git
    cd docker-compose-test
    ```

2. **Build and run the containers:**
    ```sh
    docker-compose up --build
    ```

3. **Access the application:**
    - The application will be running at `http://localhost:your_port`.

## Project Structure

- `Dockerfile`: Instructions to build the Docker image for the Python application.
- `docker-compose.yml`: Configuration file for Docker Compose to set up multiple services.
- `app/`: Directory containing the Python application code.
- `requirements.txt`: List of Python dependencies to be installed.

## Usage

### Building the Containers
To build the Docker containers, run:
```sh
docker-compose build
```

### Starting the Containers
To start the Docker containers, run:
```sh
docker-compose up
```

### Stopping the Containers
To stop the running containers, press `Ctrl+C` in the terminal where the `docker-compose up` command is running.

### Removing the Containers
To remove the stopped containers, run:
```sh
docker-compose down
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Docker documentation
- Python community
