# Log output

Generates a random UUID on startup and prints it with a UTC timestamp every 5 seconds. A Flask server returns the current timestamp and the UUID at `/`.

## Build and deploy (k3d)

The cluster needs host port 8081 mapped to the load balancer's port 80:

    k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2

Then:

    docker build -t log-output:1.7 .
    k3d image import log-output:1.7
    kubectl apply -f manifests/
    kubectl logs -f deployment/log-output

Open http://localhost:8081.

    localhost:8081 → Ingress (Traefik, port 80) → log-output-svc:2345 → pod:3000

Restart:

    kubectl rollout restart deployment/log-output
