# Production Suggestions

This project is intentionally minimal for the purpose of the assignment.  
Below are improvements that would be implemented in a production-grade setup.

---

## Security
- Use a dedicated secrets manager (e.g. HashiCorp Vault or cloud native tool i.e. Azure Key Vault)
- Store passwords hashed (bcrypt/argon2) instead of plaintext
- Enforce HTTPS via Ingress + TLS certificates
- Add authentication rate limiting and brute-force protection
- Run containers as non-root with a read-only filesystem
- Apply Kubernetes NetworkPolicies to restrict traffic
- Use Istio or Cilium to enable mTLS encrypted pod-to-pod traffic

---

## Container & Supply Chain
- Use pinned and minimal base images
- Integrate container image scanning in CI (e.g. Trivy)
- Sign images and verify signatures at deploy time
- Enforce immutable image tags in the registry

---

## CI/CD
- Build and tag images automatically on commit
- Use commit SHA-based tagging for traceability
- Run linting, tests, and security scans in pipeline
- Push images to a remote registry
- Use GitOps (e.g. ArgoCD or Flux) for deployment

---

## Kubernetes
- Use an Ingress controller instead of port-forwarding
- Define resource requests and limits
- Implement Horizontal Pod Autoscaling (HPA)
- Configure PodDisruptionBudgets
- Use separate namespaces per environment
- Externalize configuration via ConfigMaps

---

## Observability
- Implement structured logging
- Centralize logs (e.g. Loki / ELK stack)
- Expose Prometheus metrics
- Add dashboards (Grafana)
- Configure alerting for failures and resource issues

---

## Infrastructure
- Replace Kind with managed Kubernetes (e.g. EKS/GKE/AKS)
- Provision infrastructure using Terraform or similar IaC
- Use a managed database instead of SQLite
- Implement backups and disaster recovery

---

## Application
- Replace SQLite with PostgreSQL or similar
- Add database migrations
- Improve error handling and input validation
- Add automated tests
- Introduce connection pooling
- Replace custom authentication with an external identity provider (OIDC/LDAP, e.g. Keycloak)
