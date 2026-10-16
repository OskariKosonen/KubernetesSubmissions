# Ping-pong

Responds to `GET /pingpong` with `pong N`, where `N` is an in-memory request counter (resets when the pod restarts).

Shares the Ingress with [Log output](../log_output): `/pingpong` is routed here, everything else to log-output.

## Build and deploy (k3d)

    docker build -t ping-pong:1.9 .
    k3d image import ping-pong:1.9
    kubectl apply -f manifests/
    kubectl apply -f ../log_output/manifests/

Open http://localhost:8081/pingpong.

    localhost:8081/pingpong → Ingress (Traefik, port 80) → ping-pong-svc:2346 → pod:3000
