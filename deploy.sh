#!/bin/bash

gcloud run deploy cartola-python \
        --image=us-east1-docker.pkg.dev/cartola-360814/cartola-project/cartola-python@sha256:dcaf8a92b12d8f6b36cf7d56da1fc8380a7cc8953c637f3a0d922ac091344bf7 \
        --no-allow-unauthenticated \
        --port=8080 \
        --service-account=bucket-cartola@cartola-360814.iam.gserviceaccount.com \
        --memory=128Mi \
        --max-instances=1 \
        --cpu-boost \
        --region=us-central1 \
        --project=cartola-360814