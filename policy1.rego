package envoy.authz

import input.attributes.request.http as http_request 

default allow = false

allow {
    action_allowed
}

action_allowed{
  # sprintf("Found method", http_request.method)
  http_request.method == "GET"
  # sprintf("Found id", svc_spiffe_id)
  svc_spiffe_id == "spiffe://tech-talk.nutanix.com/backend_server2"
  # sprintf("Found path", http_request.path)
  glob.match("/allowed_endpoint", [], http_request.path)
}

svc_spiffe_id = spiffe_id {
    [_, _, _, uri_type_san] := split(http_request.headers["x-forwarded-client-cert"], ";")
    [_, spiffe_id] := split(uri_type_san, "=")
}