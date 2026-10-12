# Todo app

Flask web server for the course project. Serves an HTML page at `/` and prints `Server started in port NNNN` on startup. The port is set with the `PORT` environment variable (default 3000, set to 8080 in the manifest).

## Cluster (k3d)

The cluster needs host port 8081 mapped to the load balancer's port 80:

    k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2

## Build and deploy

    docker build -t todo-app:1.5 .
    k3d image import todo-app:1.5
    kubectl apply -f manifests/
    kubectl logs -f deployment/todo-app

Change the port: edit `PORT` in `manifests/deployment.yaml` and `targetPort` in `manifests/service.yaml`, then apply again.

## Access

The app is reached through an Ingress at http://localhost:8081.

    localhost:8081 → Ingress (Traefik, port 80) → todo-app-svc:1234 → pod:8080

The log output app's Ingress also uses `/`, so delete it before deploying this one:

    kubectl delete ingress log-output-ingress

For debugging without the Ingress:

    kubectl port-forward deployment/todo-app 3003:8080
