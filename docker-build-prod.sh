#!/bin/bash

docker build . --file ./docker_images/partidas.Dockerfile --tag us-east1-docker.pkg.dev/cartola-360814/cartola-project/cartola-python:0.1.11

docker push us-east1-docker.pkg.dev/cartola-360814/cartola-project/cartola-python:0.1.11