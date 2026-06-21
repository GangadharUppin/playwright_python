https://www.youtube.com/watch?v=UC2wj3Bg3eM&list=PLqndseDs9rmIwtzB1i08UWkQjQhpmZhtH
there are 2 api's in playwright 
1. sync -> it works as normal python code
2. async ->  it uses the async and wait keyword to control flow of execution.
pip install pytest-playwright




# CI/CD (GitHub Actions → Argo CD) — notes

Overview
- CI job (GitHub Actions) runs tests, builds a container image and pushes it to a registry.
- The same job updates the Kubernetes manifest (or kustomize file) with the new image tag OR the image tag update can be done by an image updater tool.
- Argo CD monitors a single directory in this repo (e.g., `/k8s` or `/argo`) and syncs those Kubernetes manifests to the cluster.
- To make Argo CD only deploy what you want, place only the manifests you want it to manage in that directory and point the Argo CD Application to that path.

High-level flow
1. Developer pushes code → GitHub Actions runs tests.
2. On success, action builds an image (tagged with the commit SHA) and pushes to the registry.
3. Action updates the k8s manifest in the repo (or updates kustomize), committing the new image tag.
4. Argo CD detects the repo change (or monitors the repo branch) and applies the manifests from the configured path to the cluster.
5. Optionally enable Argo CD Auto-Sync to automatically apply changes.

Why Argo CD looks at what you want
- Argo CD does not automatically scan your whole repository for an argo.yaml file.
- Argo CD applies whatever manifests are exposed by an Application resource. You either:
  - Create an Argo CD Application resource (apply argo-app.yaml to the cluster), or
  - Register the repository in the Argo CD UI / CLI and create an application via the UI where you specify repo URL + path.
- The Application’s spec.source.path is the directory Argo CD will monitor. To ensure Argo CD only deploys the manifest(s) you intend:
  - Put those manifests in their own directory (e.g., /k8s/playwright-python/) and set spec.source.path to that directory, or
  - Use kustomize in that directory and list exactly the resources you want in kustomization.yaml.

Pod / Deployment manifest — how it’s pointed
- The pod (Deployment) manifest lives in the repo directory Argo CD is configured to watch.
- The Argo CD Application's spec.source.path points to that directory. Example:
  spec:
    source:
      repoURL: https://github.com/your/repo.git
      path: k8s/playwright-python
      targetRevision: HEAD
- Argo CD scans all YAML manifests in that path and applies them. So the Deployment file is discovered by Argo CD because it exists inside the path you configured.

Important details & suggestions
- Keep manifests for different apps in separate directories to avoid accidental cross-deploys.
- Use image tags tied to commit SHA (immutable) to ensure reproducible deploys.
- To update images automatically you can:
  - Commit the updated manifest from the GitHub Action (simple),
  - Use Argo CD Image Updater (adds automation to update image tags in GitHub when new images are pushed),
  - Or use kustomize image transformer in the repo and update kustomization.yaml via the action.
- Store registry credentials in:
  - GitHub Actions secrets (for the build step), and
  - Kubernetes imagePullSecrets or configure the registry credentials in Argo CD (if Argo CD needs to read charts/Helm from private registries).
- Namespace / RBAC: ensure the service account Argo CD uses has permissions in the target namespace(s).

