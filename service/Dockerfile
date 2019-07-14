FROM envoyproxy/envoy-alpine:v1.11.0

RUN apk update && apk add python3 bash curl
RUN pip3 install -q Flask==0.11.1 requests==2.18.4
RUN mkdir /code
ADD ./service.py /code
ADD ./start_service.sh /usr/local/bin/start_service.sh
RUN chmod u+x /usr/local/bin/start_service.sh
COPY envoy_s_1.yaml envoy_s_2.yaml envoy_s_3.yaml envoy_s_4.yaml /etc/
ENTRYPOINT /usr/local/bin/start_service.sh