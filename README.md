# docker_flask_homework

## Installing Docker locally 
1. Click [here](https://hub.docker.com/) to go to the Docker Hub website and download Docker Desktop.
2. Follow the instructions to install Docker Desktop and setup your Docker Hub account.
3. Go to VS Code and install the Docker extension.

## The process of Dockerizing the applications in both parts
### Part1
1. Create a basic Flask application with a requirements.txt file.
2. Create a Dockerfile.
3. Build the image using the command `docker build -t <image_name> .` 
4. Run the image using the command `docker run-p 5000:5000 <image_name>`; run the image in the background using the command `docker run -d -p 5000:5000 <image_name>`.
5. Use the command `docker ps` to check if the image is running, and use the command `docker stop <container_id>` to stop the image.
6. Delete the image using the command `docker system prune -f -a`.
### Part2
1. Create one folder for each application. Each folder contains a Dockerfile and a requirements.txt file.
2. Outside the folders, create a docker-compose.yml file.
3. Build the containers using the command `docker-compose up --build`.
4. Use the command `docker-compose down` to stop the containers.
5. Remove containeres using the command `docker-compose rm`.

## Observations, challenges faced, and reflections on the use of Docker and Docker Compose.
- Docker containers contain applications and all their dependencies, so they can be run on any computer on any environment. This helps developers to prevent conflicts between dependencies and to run applications on different environments.
- Docker Compose is a tool for defining and running multi-container Docker applications. It allows developers to run multiple containers for multipel applications at the same time. 


