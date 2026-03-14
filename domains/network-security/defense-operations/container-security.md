# 🛡️ Container & Kubernetes Security: Modern Attack Techniques

> Nội dung: Docker escape, Kubernetes RBAC abuse, image scanning pipeline, runtime defense.

---

## 1. Container Threat Landscape
- Supply chain image bẩn → chạy trong cluster production.
- Privileged container & hostPath mount mở đường escape.
- Kubernetes API exposed với RBAC lỏng lẻo.

---

## 2. Docker Escape Techniques

| Vector | Mô tả | Mitigation |
| --- | --- | --- |
| Privileged container | `--privileged` + mount `/` -> attacker chroot host | Cấm privileged, sử dụng PodSecurityPolicy/OPA Gatekeeper |
| Capabilities | `CAP_SYS_ADMIN`, `CAP_DAC_READ_SEARCH` → break isolation | Drop all, add tối thiểu |
| Device mount | `/dev/kmsg`, `/var/run/docker.sock` → control host engine | NetworkPolicy + Admission controller block |

### Checklist
- [ ] `docker info` → Rootless mode?
- [ ] Enable seccomp/apparmor profiles.
- [ ] Read-only root filesystem cho container không cần write.

---

## 3. Kubernetes RBAC & API Server

### 3.1 Common Misconfig
- `cluster-admin` role gán cho service account default.
- API server lộ ra Internet (`0.0.0.0:6443`).

### 3.2 Attack chain
1. Compromise pod → steal service account token `/var/run/secrets/kubernetes.io/serviceaccount/token`.
2. Use token call API → escalate quay `kubectl get secrets`.
3. Create privileged pod → escape host.

### 3.3 Defense
- Implement RBAC least privilege (`Role` + `RoleBinding`).
- Rotate service account token, disable automount nếu không cần.
- API server behind private network + authentication (mTLS + OIDC).

---

## 4. Image Scanning & Supply Chain

- Use trusted base image, pin digest (`image: nginx@sha256:...`).
- Scan with Trivy/Grype trong CI/CD.
- Signed image bằng Cosign, enforce policy (Kyverno `verifyImages`).

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-signed-images
spec:
  validationFailureAction: enforce
  rules:
    - name: verify-signature
      match:
        resources:
          kinds:
            - Pod
      verifyImages:
        - imageReferences:
            - "registry.example.com/*"
          attestors:
            - entries:
                - keys:
                    publicKeys: |
                      -----BEGIN PUBLIC KEY-----
```

---

## 5. Runtime Detection
- Falco rule: detect `apk add`, `apt install` inside container.
- eBPF-based Cilium Tetragon để log syscalls.
- Monitor `kubectl exec` theo Audit log.

```yaml
- rule: Write below etc
  desc: Detect file write below /etc
  condition: evt.type in (open,openat) and fd.directory="/etc"
```

---

## 6. Incident Response
1. Snapshot affected Pod (kubectl cp logs, containerd snapshot).
2. Quarantine namespace bằng NetworkPolicy deny-all.
3. Rotate secrets, regenerate service account token.

> ✅ Checklist cuối:
- [ ] Admission control enforce securityContext.
- [ ] Image signing + vulnerability scanning trong CI/CD.
- [ ] RBAC audit: không có binding cluster-admin vĩnh viễn.
- [ ] Runtime detection (Falco/eBPF) + alert pipeline.
- [ ] Disaster recovery playbook nếu node compromise.