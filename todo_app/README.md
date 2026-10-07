# Todo app

Flask web server for the course project. Serves an HTML page at `/` and prints `Server started in port NNNN` on startup. The port is set with the `PORT` environment variable (default 3000).

## Build and deploy (k3d)

    docker build -t todo-app:1.5 .
    k3d image import todo-app:1.5
    kubectl apply -f manifests/deployment.yaml
    kubectl logs -f deployment/todo-app

Change the port: edit `PORT` in `manifests/deployment.yaml` and apply it again.

## Access

    kubectl port-forward deployment/todo-app 3003:8080

Then open http://localhost:3003.
