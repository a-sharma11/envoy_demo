#!/bin/sh

envoyFile=envoy_s_${SERVICE_NAME}.yaml
python3 /code/service.py &
envoy -l debug -c /etc/$envoyFile --service-cluster service${SERVICE_NAME}