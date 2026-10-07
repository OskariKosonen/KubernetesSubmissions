# Todo app

Flask web server for the course project. Prints `Server started in port NNNN` on startup. The port is set with the `PORT` environment variable (default 3000).

## Build and deploy (k3d)

    docker build -t todo-app:1.2 .
    k3d image import todo-app:1.2
    kubectl create deployment todo-app --image=todo-app:1.2
    kubectl logs -f deployment/todo-app

Change the port:

    kubectl set env deployment/todo-app PORT=8080
