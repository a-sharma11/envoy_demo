from flask import Flask
from flask import request
import os
import requests
import socket
import sys

app = Flask(__name__)

TRACE_HEADERS_TO_PROPAGATE = [
    'X-Ot-Span-Context',
    'X-Request-Id',

    # Zipkin headers
    'X-B3-TraceId',
    'X-B3-SpanId',
    'X-B3-ParentSpanId',
    'X-B3-Sampled',
    'X-B3-Flags',

    # Jaeger header (for native client)
    "uber-trace-id"
]


@app.route('/service/<service_number>')
def hello(service_number):
  return ('Hello from behind Envoy (service {})! hostname: {} resolved'
          'hostname: {}\n'.format(os.environ['SERVICE_NAME'], socket.gethostname(),
                                  socket.gethostbyname(socket.gethostname())))


@app.route('/trace/<service_number>')
def trace(service_number):
  headers = {}
  # call service 2 from service 1
  service_instance = int(os.environ['SERVICE_NAME'])
  downStreamResponse = ''
  if service_instance < 4:
    for header in TRACE_HEADERS_TO_PROPAGATE:
      if header in request.headers:
        headers[header] = request.headers[header]
    ret = requests.get("http://localhost:9000/trace/" + str(service_instance + 1), headers=headers)
    if ret.status_code != 200:
      return "ERROR. Status Code:" + str(ret.status_code), ret.status_code
    downStreamResponse = ret.text
  
  return '-> From Service: ' + str(service_instance) + downStreamResponse


if __name__ == "__main__":  
  app.run(host='127.0.0.1', port=8080, debug=True)
