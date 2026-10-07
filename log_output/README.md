# Log output

Generates a random UUID on startup and prints it with a UTC timestamp every 5 seconds.

## Build and deploy (k3d)

    docker build -t log-output:1.1 .
    k3d image import log-output:1.1
    kubectl apply -f manifests/deployment.yaml
    kubectl logs -f deployment/log-output

Restart:

    kubectl rollout restart deployment/log-output
