docker stop selenoid && docker rm selenoid 
docker stop selenoid-ui && docker rm selenoid-ui
docker run -d --name selenoid -p 4444:4444 -v /var/run/docker.sock:/var/run/docker.sock -v ${PWD}/selenoid/config:/etc/selenoid/:ro -v /data/selenoid/video:/opt/selenoid/video -v /data/selenoid/logs:/opt/selenoid/logs -e OVERRIDE_VIDEO_OUTPUT_DIR=/data/selenoid/video aerokube/selenoid:latest-release -limit 50 -video-output-dir /opt/selenoid/video -timeout 2m
docker run -d --name selenoid-ui -p 8080:8080 aerokube/selenoid-ui --selenoid-uri http://${DOCKER_GATEWAY_ADDR}:4444 -allowed-origin "*"
