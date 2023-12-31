#!/bin/bash

docker build -t python_teste .

docker tag python_teste local_image
docker tag python_teste us-east1-docker.pkg.dev/cartola-360814/cartola-project/cartola-python:0.1.5

docker push us-east1-docker.pkg.dev/cartola-360814/cartola-project/cartola-python:0.1.5