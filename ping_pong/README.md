# Ping-pong

Responds to `GET /pingpong` with `pong N`, where `N` is a request counter. The count is also saved to `pingpong.txt` on the shared persistent volume ([volumes](../volumes)), where Log output reads it.

Shares the Ingress with [Log output](../log_output): `/pingpong` is routed here, everything else to log-output.

## Build and deploy (k3d)

    docker build -t ping-pong:1.11 .
    k3d image import ping-pong:1.11
    kubectl apply -f ../volumes/
    kubectl apply -f manifests/
    kubectl apply -f ../log_output/manifests/

Open http://localhost:8081/pingpong.

    localhost:8081/pingpong → Ingress (Traefik, port 80) → ping-pong-svc:2346 → pod:3000
