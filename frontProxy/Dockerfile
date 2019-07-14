FROM envoyproxy/envoy-alpine:v1.11.0

COPY front-proxy.yaml /etc/front-envoy.yaml

CMD ls /etc/front-envoy.yaml && /usr/local/bin/envoy -l debug -c /etc/front-envoy.yaml
