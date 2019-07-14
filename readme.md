Setup includes 4 python services and 1 front proxy.

To Run:

1. ``docker-compose up --build``
2. open bash and run: ``curl 'http://localhost:8000/trace/1' -H 'X-Request-Id: 8cda17a5-eb41-4ced-9843-acc826f95c8c'``
3. Check logs of front-proxy: ``docker ps`` to get the container id of the front-proxy and run: ``docker logs {containerId}``
4. Check the x-request-id. It would be ``8cda17a5-eb41-9ced-9843-acc826f95c8c``