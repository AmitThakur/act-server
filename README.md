# Adaptive Coding Tutor-Server

## Steps:

1. Build a docker image.
    ```shell
    docker build -t act-server .
    ```
2. Run the server:
    ```commandline
    docker run -d --name act-server-container -p 80:80 act-server
    ```
3. List the running docker containers:
    ```
   docker ps
   ```
4. Stop the container (by name or id):
    ```
   docker stop act-server-container
   ```
5. Remove the container by name:
    ```commandline
    docker rm act-server-container
    ```
