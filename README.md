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

The following screenshots show the actual implementation, deployment, testing, and verification completed during this project.

### 🔄 GitHub Actions CI/CD

![GitHub Actions CI/CD](<output images/CICD check.png>)

The GitHub Actions workflow automatically builds the Docker image and deploys the application to Kubernetes.  
The final pipeline completed successfully with all major deployment and verification steps passing.

---

### 🐳 Docker Container

![Docker Container](<output images/docker container check.png>)

The backend application was successfully packaged and executed as a Docker container.  
This helped create a consistent environment for running the application locally and in Kubernetes.

---

### 🐳 Docker Images

![Docker Images](<output images/docker images check.png>)

The application Docker images were built and tagged with version numbers.  
The images were also pushed to Docker Hub for use during Kubernetes deployment.

---

### ☸️ Kubernetes Deployment

![Kubernetes Deployment](<output images/deploy to kuber.png>)

The Healthletic backend was deployed to a local Kubernetes cluster using Helm.  
The deployment was verified by checking pods, services, and deployment status.

---

### ☸️ Kubernetes Pods & Services

![Kubernetes Pods and Services](<output images/Screenshot 2026-08-15 161431.png>)

The Kubernetes pods were running successfully with `1/1` containers ready.  
The backend service was available inside the `healthletic` namespace on port `5000`.

---

### ⎈ Helm Deployment

![Helm Deployment](<output images/Screenshot 2026-08-15 161529.png>)

Helm was used to install and upgrade the Healthletic backend deployment.  
Helm release revisions were checked to confirm successful deployments.

---

### 🔍 Kubernetes Verification

![Kubernetes Verification](<output images/Screenshot 2026-08-15 162252.png>)

Kubernetes resources were verified using commands such as `kubectl get pods`, `kubectl get deployment`, and `kubectl get service`.  
The application remained in a healthy `Running` state without pod restarts.

---

### ❤️ API Health Check

![API Health Check](<output images/moke tet Screenshot 2026-08-15 164637.png>)

The `/health` endpoint was tested after deployment using `curl`.  
The API returned HTTP `200` with a healthy application status.

---

### 🗄️ Database Smoke Test

![Database Smoke Test](<output images/Database check.png>)

The SQLite database was tested from inside the running Kubernetes pod.  
The query returned `DATABASE OK`, confirming that database access was working.

---

### 📊 Application Logs

![Application Logs](<output images/Screenshot 2026-08-15 165537.png>)

Application logs show successful requests to the `/health` endpoint.  
The HTTP `200` responses confirm that the deployed backend was responding correctly.

---

### 🐳 Docker Hub

![Docker Hub](<output images/Screenshot 2026-08-15 220826.png>)

The Docker image was published to Docker Hub with versioned tags.  
This image was used as the container image for the Kubernetes deployment.

## 👨‍💻 About Me

I'm **Ashwath Amudhan C A**, a Computer Science graduate interested in **DevOps and Cloud Engineering**.

This project helped me gain hands-on experience with **Docker, Kubernetes, Helm, GitHub Actions, CI/CD, Linux/command-line troubleshooting, and cloud/DevOps practices**.

---

⭐ If you find this project useful, feel free to explore the repository.
