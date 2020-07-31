# (yet another) reverse https proxy

This little program can do TLS termination for HTTPS traffic and forwards requests using HTTP request for which the X-Forwarder-* headers are set. It was created for providing HTTPs access to a Jenkins docker image.

    go run https-proxy.go -v -front :443 -back :8080 -cert domain.com-chain.pem -key domain.com-key.pem

## non-TLS usage

    go run https-proxy.go -v -front :443 -back :8080 -stripprefix /hello
