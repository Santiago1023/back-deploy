# BackendSignAI


## To build docker image:
docker build -t signai .

## To run docker container
docker run -d --name signaicontainer -p 80:80 signai

## To see logs in the container
docker logs signaicontainer

##  To delete image container
docker rm signaicontainer