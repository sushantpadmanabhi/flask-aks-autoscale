# flask-aks-autoscale

# Flask App on Azure Kubernetes Service (AKS) with Docker, Load Balancing & Auto-Scaling

This project demonstrates how to containerize a Python Flask application using Docker, deploy it to Azure Kubernetes Service (AKS), expose it using a LoadBalancer, and configure autoscaling using the Horizontal Pod Autoscaler (HPA).

---

## 🚀 Features

* Simple Flask app with CPU load simulation endpoint
* Dockerized and stored in Azure Container Registry (ACR)
* Deployed to Azure Kubernetes Service (AKS)
* LoadBalanced external access via Kubernetes Service
* HPA scaling based on CPU utilization
* Monitored via Azure Monitor Insights

---

## 🔧 Technologies Used

* Python (Flask)
* Docker
* Azure Container Registry (ACR)
* Azure Kubernetes Service (AKS)
* kubectl & Azure CLI
* Horizontal Pod Autoscaler
* Azure Monitor Insights

---

## 📄 Project Structure

```bash
flask-cpu-app/
│
├── app.py                # Flask application code
├── Dockerfile            # Docker build file
├── deployment.yaml       # Kubernetes deployment config
├── service.yaml          # Kubernetes service config (LoadBalancer)
├── hpa.yaml              # Horizontal Pod Autoscaler config
└── README.md             # Project documentation
```

---

## 🔬 Step-by-Step Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/flask-aks-autoscale.git
cd flask-aks-autoscale
```

### 2. Build and Push Docker Image to ACR

```bash
docker build -t <youracr>.azurecr.io/flask-cpu-app:latest .
docker push <youracr>.azurecr.io/flask-cpu-app:latest
```

### 3. Create AKS Cluster (if not already done)

```bash
az aks create \
  --resource-group myResourceGroup \
  --name flaskAKSCluster \
  --node-count 2 \
  --enable-addons monitoring \
  --generate-ssh-keys \
  --attach-acr <youracr>
```

### 4. Connect to AKS Cluster

```bash
az aks get-credentials --resource-group myResourceGroup --name flaskAKSCluster
kubectl get nodes
```

### 5. Deploy Application

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
```

### 6. Access the App

```bash
kubectl get svc flask-cpu-service
# Use the EXTERNAL-IP shown:
http://<EXTERNAL-IP>/        # Returns 'Hello from AKS!'
http://<EXTERNAL-IP>/load    # Triggers 15-second CPU spike
```

### 7. Monitor and Test HPA

```bash
kubectl get hpa
kubectl top pods
```

PowerShell loop to simulate CPU load:

```powershell
for ($i = 1; $i -le 20; $i++) {
    Invoke-WebRequest -Uri "http://<EXTERNAL-IP>/load" -UseBasicParsing
    Start-Sleep -Seconds 2
}
```

---

## 📊 Monitoring

* Navigate to AKS Cluster in Azure Portal
* Go to **Monitoring > Insights > Cluster / Controllers / Workloads**
* View CPU usage graphs, pod counts, and scaling events

---

## 🚮 Cleanup

To avoid charges:

```bash
az group delete --name myResourceGroup --yes --no-wait
```

---

## 📖 Screenshots (Attach in Repo)

* HPA scaling activity from Azure Monitor
* Pod CPU usage and LoadBalancer response
* Cluster metrics dashboards

---

## 📆 Author

**Your Name**
LinkedIn: [Your LinkedIn](https://linkedin.com/in/your-profile)
GitHub: [Your GitHub](https://github.com/yourusername)

---

## ✨ Future Enhancements

* Memory-based HPA
* CI/CD with Azure DevOps Pipelines
* Prometheus + Grafana dashboards
* Ingress controller with SSL

---

> This project is a hands-on showcase of AKS autoscaling, monitoring, and deployment practices for containerized apps in Azure.
