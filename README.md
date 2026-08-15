# 🏥 Healthletic Backend — DevOps CI/CD

A simple **DevOps project** where I containerized a Python/Flask backend, automated the build and deployment with **GitHub Actions**, and deployed it to **Kubernetes using Helm**.

The project also includes API and SQLite database smoke tests.

## 🚀 CI/CD Flow

```text
GitHub
  ↓
GitHub Actions
  ↓
Docker Build
  ↓
Trivy Scan
  ↓
Docker Hub
  ↓
Kubernetes + Helm
  ↓
API & Database Smoke Tests
```

## 🛠️ Tech Stack

- 🐍 Python / Flask
- 🐳 Docker
- ☸️ Kubernetes
- ⎈ Helm
- 🔄 GitHub Actions
- 🔐 Trivy
- 🗄️ SQLite
- 📦 Docker Hub
- 🪟 Windows Self-Hosted Runner

## 📂 Project Structure

```text
healthletic-devops-assessment/
├── .github/workflows/
├── helm/backend/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🐳 Docker

Build the image:

```powershell
docker build -t ashwathamudhan/healthletic-backend:v1.0.13 .
```

Run locally:

```powershell
docker run -p 5000:5000 ashwathamudhan/healthletic-backend:v1.0.13
```

Docker Hub:

`ashwathamudhan/healthletic-backend`

## ☸️ Kubernetes + Helm

Deploy:

```powershell
helm upgrade --install healthletic-backend .\helm\backend `
  --namespace healthletic `
  --create-namespace `
  --set image.repository=ashwathamudhan/healthletic-backend `
  --set image.tag=v1.0.13 `
  --wait `
  --timeout 5m
```

Check deployment:

```powershell
kubectl get pods -n healthletic
kubectl get deployment -n healthletic
kubectl get service -n healthletic
helm list -n healthletic
```

Expected pod status:

```text
1/1 Running
```

## ❤️ API Health Check

Port forward the Kubernetes service:

```powershell
kubectl port-forward service/healthletic-backend 18081:5000 -n healthletic
```

Test the API:

```powershell
curl.exe http://localhost:18081/health
```

Expected response:

```json
{
  "application": "healthletic-backend",
  "status": "healthy",
  "version": "v1.0.0"
}
```

## 🗄️ Database Check

SQLite was verified from inside the running Kubernetes pod:

```powershell
kubectl exec -it <POD_NAME> -n healthletic -- python -c "import sqlite3; c=sqlite3.connect('healthletic.db'); c.execute('SELECT 1'); print('DATABASE OK'); c.close()"
```

Result:

```text
DATABASE OK
```

## ✅ Final Result

The final GitHub Actions run successfully completed:

- ✅ Docker build
- ✅ Kubernetes deployment
- ✅ Helm deployment
- ✅ Pod readiness
- ✅ API smoke test
- ✅ Database smoke test
- ✅ Deployment verification

## 📸 Project Evidence

### GitHub Actions — Successful CI/CD

![CI/CD](docs/screenshots/api-database-smoke-test.png)

### Kubernetes Deployment

![Kubernetes](docs/screenshots/kubernetes-status.png)

### Kubernetes Pods & Services

![Kubernetes verification](docs/screenshots/kubernetes-status-detail.png)

### Docker & Helm

![Docker and Helm](docs/screenshots/docker-helm-deployment.png)

### Helm / Kubernetes Verification

![Helm verification](docs/screenshots/helm-kubernetes-verification.png)

### Application Health Logs

![API logs](docs/screenshots/api-logs-and-pods.png)

### Docker Hub

![Docker Hub](docs/screenshots/docker-hub-images.png)

## 👨‍💻 About Me

I'm **Ashwath Amudhan C A**, a Computer Science graduate interested in **DevOps and Cloud Engineering**.

This project helped me gain hands-on experience with **Docker, Kubernetes, Helm, GitHub Actions, CI/CD, Linux/command-line troubleshooting, and cloud/DevOps practices**.

---

⭐ If you find this project useful, feel free to explore the repository.
