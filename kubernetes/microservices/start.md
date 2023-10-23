```bash
minikube delete && \
minikube start && \
kubectl create -f namespaces/ && \
kubectl create -f deployments && \
kubectl create -f services/

kubectl get all -n vote

minikube service result --url -n vote
minikube service vote --url -n vote
```