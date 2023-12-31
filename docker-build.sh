#!/bin/bash

docker build --platform linux/amd64 -t cartola_local .

docker tag cartola_local local_image
docker tag cartola_local us-east1-docker.pkg.dev/cartola-360814/cartola-project/cartola-python:0.1.11

docker push us-east1-docker.pkg.dev/cartola-360814/cartola-project/cartola-python:0.1.11