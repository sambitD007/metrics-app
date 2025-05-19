# metrics-app
A stateful app which keeps track of api call made at /counter endpoint

docker build -t metrics-app .
docker run -e PASSWORD=MYPASSWORD -p 80:80 --name metrics-app metrics-app
echo pat-token | docker login ghcr.io -u username --password-stdin
docker tag metrics-app:latest ghcr.io/username/metrics-app:0.1
docker push ghcr.io/username/metrics-app:0.1
