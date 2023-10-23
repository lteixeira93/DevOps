minikube stop
minikube start
minikube status
kubectl get nodes
kubectl get pods -A

# Management layer commands:
kube-apiserver # Which pods are being executed and their state
etcd # Store data in management cluster (Backup and data)
kube-scheduler # Assign pod to node based on available resources
kube-controller-manager # Daemon which uses kube-apiserver and update status
kubeadm # Command to create clusters locally
kubelet # Initialize pods and container
kubectl # interatction with cluste

Amazon EKS - Creates our master node (aka control plane)
OR
Gogle GKE (Google kubernetes engine)

KUBECTL -> AMAZON EKS
            |   |   |
            n0  n1  nn

sudo apt install google-cloud-cli-gke-gcloud-auth-plugin1
gcloud container clusters get-credentials cluster-ltx --zone us-central1-c --project confident-pen-391018
kubectl get nodes

Steps:
Create cluster -> Implant app ->

Yml configure pods

# Run your pod locally
kubectl apply -f pod.yaml

# List pods
kubectl get pod -o wide

# Access pod
minikube ssh

tx@DESKTOP-TQ5N5OV:~/projects/kubernetes/pod$ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

ltx@DESKTOP-TQ5N5OV:~/projects/kubernetes/pod$ kubectl get nodes
NAME       STATUS   ROLES           AGE     VERSION
minikube   Ready    control-plane   5h15m   v1.26.3
ltx@DESKTOP-TQ5N5OV:~/projects/kubernetes/pod$ kubectl get pods
NAME       READY   STATUS    RESTARTS   AGE
app-html   1/1     Running   0          18s

app-html is-a container


kubectl get pod <name>

describe node hardware
kubectl describe node minikube
kubectl explain deploy

kubectl get deployment
kubectl describe deployment app-html-deployment
kubectl scale deployment app-html-deployment --replicas=10
kubectl expose deployment app-jtml-deployment --type=LoadBalancer --name=app-html --port80
ltx@DESKTOP-TQ5N5OV:~/projects/kubernetes/pod$ kubectl get service
NAME         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
app-html     LoadBalancer   10.103.30.42   <pending>     80:31342/TCP   13s
kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP        28h

minikube service --url app-html # Return ip to access app, each request is redirected to some pod

# Connects to GCP to kubectl
gcloud container clusters get-credentials cluster-ltx --zone us-central1-c --project confident-pen-391018
"""
Fetching cluster endpoint and auth data.
kubeconfig entry generated for cluster-ltx.
"""
kubectl apply -f pod.yml
gcloud init
gcloud compute instances list