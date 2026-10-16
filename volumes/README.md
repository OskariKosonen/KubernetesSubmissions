# Shared volume

PersistentVolume and PersistentVolumeClaim shared by [Log output](../log_output) and [Ping-pong](../ping_pong).

The volume is a local directory `/tmp/kube` on node `k3d-k3s-default-agent-0`. Create it first and make it writable for the containers (they run as `nobody`):

    docker exec k3d-k3s-default-agent-0 sh -c "mkdir -p /tmp/kube && chmod 777 /tmp/kube"
    kubectl apply -f volumes/
