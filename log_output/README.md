# Log output

One pod with two containers sharing an `emptyDir` volume mounted at `/usr/src/app/files`:

- **writer** generates a random UUID on startup and appends a line with a UTC timestamp and the UUID to `log.txt` every 5 seconds.
- **reader** is a Flask server that returns the contents of `log.txt` at `/`.

## Build and deploy (k3d)

The cluster needs host port 8081 mapped to the load balancer's port 80:

    k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2

Then:

    docker build -t log-output-writer:1.10 writer
    docker build -t log-output-reader:1.10 reader
    k3d image import log-output-writer:1.10 log-output-reader:1.10
    kubectl apply -f manifests/
    kubectl logs -f deployment/log-output -c log-output-writer

Open http://localhost:8081.

    localhost:8081 → Ingress (Traefik, port 80) → log-output-svc:2345 → reader:3000

Restart:

    kubectl rollout restart deployment/log-output
