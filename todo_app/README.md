# Todo app

Flask web server for the course project. Serves an HTML page at `/` and prints `Server started in port NNNN` on startup. The port is set with the `PORT` environment variable (default 3000, set to 8080 in the manifest).

## Cluster (k3d)

The cluster needs host port 8082 mapped to NodePort 30080:

    k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2

## Build and deploy

    docker build -t todo-app:1.5 .
    k3d image import todo-app:1.5
    kubectl apply -f manifests/
    kubectl logs -f deployment/todo-app

Change the port: edit `PORT` in `manifests/deployment.yaml` and `targetPort` in `manifests/service.yaml`, then apply again.

## Access

The NodePort Service `todo-app-svc` exposes the app on node port 30080, which k3d maps to http://localhost:8082.

    localhost:8082 → node:30080 (NodePort) → todo-app-svc → pod:8080

For debugging without the Service:

    kubectl port-forward deployment/todo-app 3003:8080
