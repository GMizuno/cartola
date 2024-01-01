#!/bin/bash

gcloud run jobs create partidas-71 \
      --image=us-east1-docker.pkg.dev/cartola-360814/cartola-project/cartola-python-matchs-teams:3b1669a8deb6013d771cf72045021777fdaa0d42ed0a771f4a69235a04a67363 \
      --service-account=cartola-projeto-python@cartola-360814.iam.gserviceaccount.com \
      --set-env-vars=API_HOST_KEY=1,API_SECERT_KEY=2,LEAGUE_ID=71,SEASON_YEAR=2023 \
      --region=us-central1 \
      --project=cartola-360814 \
      --tasks=1 \
      --max-retries=2 \
      --parallelism=1

gcloud scheduler jobs update http partidas-71 \
  --location us-central1 \
  --schedule="0 15 * * *" \
  --uri="https://us-central1-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/cartola-360814/jobs/partidas:run" \
  --http-method POST \
#  --oauth-service-account-email cartola-projeto-python@cartola-360814.iam.gserviceaccount.com

gcloud run jobs delete --region us-central1 --quiet partidas-71
