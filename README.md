# An example Dockerfile for undetected-chromedriver

This Dockerfile builds an image with undetected-chromedriver and a VNC server.
The entrypoint ensures that the VNC server is running before the script is executed.
To execute your script you should mount the `mount` directory into the containers `/opt/wd`
directory.

Example command to build and run the container:
```bash
docker build -t undetected-chromedriver . && docker run -it --rm --volume ./mount:/opt/wd --name undetected-chromedriver -e VNC_PASSWORD=123456 -p 5900:5900 undetected-chromedriver python start.py
```
The VNC server is now accessible on localhost:5900 with password 123456
You could also use the docker-compose.yml file.
