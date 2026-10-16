# Volumes

- `shared-pv` / `shared-claim`: shared by [Log output](../log_output) and [Ping-pong](../ping_pong), directory `/tmp/kube`.
- `todo-pv` / `todo-claim`: image cache for the [Todo app](../todo_app), directory `/tmp/kube-todo`.

Both are local directories on node `k3d-k3s-default-agent-0`. Create them first and make them writable for the containers (they run as `nobody`):

    docker exec k3d-k3s-default-agent-0 sh -c "mkdir -p /tmp/kube /tmp/kube-todo && chmod 777 /tmp/kube /tmp/kube-todo"
    kubectl apply -f volumes/
