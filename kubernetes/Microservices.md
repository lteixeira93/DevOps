# Notes
```docker
Best practice: POD_NAME name same as IMAGE_NAME

Kubernetes always contains 4 top level entries
apiVersion
kind
metadata
spec

Minikube creates just one cluster containing master and worker with all functions

Best implementation is each POD with 1 container 1:1

Best strategy is RollingUpdate

Each service in their own container

Docker assign IP for each container in the same docker network

Kubernetes assign IP for each POD in the cluster

Do not create POD communications by using IP address since it may change

FQDN is full service information

Microservices and scalability (Vertical (Memory, disk upgrades) or Horizontal (More clusters))

Microservices example: https://github.com/guniversityBR/example-voting-app.git
```
## Cluster info
```docker
kubectl cluster-info

Kubernetes control plane is running at https://127.0.0.1:32769
CoreDNS is running at https://127.0.0.1:32769/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

## Creating POD
```docker
# Best practice: POD_NAME name same as IMAGE_NAME
kubectl run <POD_NAME> --image <IMAGE_NAME>
```

## Creating namespace
```docker
kubectl create -f pods/yaml --save-config --namespace=frontend
```

## Get namespaces
```docker
# Best practice: POD_NAME name same as IMAGE_NAME
kubectl get namespaces
```

## Verify all PODs
```docker
kubectl get pods -o wide
```

## Describe POD
```docker
kubectl describe pod <POD_NAME>
```

## Kubernetes YAML
```YAML
# Always contains these 4 top level entries
apiVersion:
kind:
metadata:
spec:

# Where

apiVersion can be
# POD:          v1
# SERVICE:      v1
# REPLICA_SET:  apps/v1
# DEPLOYMENT:   apps/v1

kind can be
# Pod
# Service
# replica
# deployment

metadata can be
# name: app-name
# label: app-label
# app: app
# These names shall be supported by kubernetes (see: https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/)

spec can be
# Specifications of kubernetes object to be created
# containers:
    # - name:
    # - image:
```

## Create POD
```docker
kubectl create/apply -f <YAML_FILENAME> --save-config
```

## Get replication controllers
```docker
kubectl get replicationcontroller
```

## Get deployments
```docker
kubectl get deployments
```

## Get replicas
```docker
kubectl get replicaset
```

## Get all
```docker
kubectl get all
```

## Delete replica
```docker
kubectl delete replicaset <REPLICA_NAME>
```

## Scale replica manually
```docker
kubectl scale --replicas=X -f <YAML_FILENAME>
```

## Delete whole cluster
```docker
minikube delete
```

## Rollout info
```docker
kubectl rollout status deployment/frontend-dp
kubectl rollout history deployment/frontend-dp
```

## Undo update
```docker
kubectl rollout undo deployment/frontend-dp
```

## Create deployment with record reason enabled
```docker
kubectl create -f deployments/frontend.yaml --save-config --record
```

## Accessing POD shell
```docker
kubectl exec -it <POD_NAME> -- bash
```

## Get all cluster info
```docker
kubectl get all -n kube-system
```

## Connect to mysql present in another pod
```docker
apt search mysql-client

---

10.244.0.3 (mysql POD IP)
```
```bash
mysql -h 10.244.0.3 -u root -p myPass

root@webapp-5db44756bc-lhq6t:/# mysql -h 10.244.0.3 -uroot -pmyPass geek
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.42 MySQL Community Server (GPL)

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [geek]> create table pessoas (id int primary key auto_increment, nome varchar(255), email varchar(255));
MySQL [geek]> show tables;
+----------------+
| Tables_in_geek |
+----------------+
| pessoas        |
+----------------+
ctrl+d -> leave pod
```

## Connect to mysql present in another pod
```docker
cat /etc/resolv.conf 
```

```
-> nameserver 10.96.0.10
search default.svc.cluster.local svc.cluster.local cluster.local
options ndots:5
```

## Fully qualified domain name (FQDN) of Kubernetes
```bash
apt install dnsutils
```
```bash
nslookup kubernetes
Server:         10.96.0.10
Address:        10.96.0.10#53

Name:   kubernetes.default.svc.cluster.local (FQDN)
        (SERVICE)(NAMESPACE)(KIND)(CLUSTER_NAME)
Address: 10.96.0.1
```

## Service types
```bash
NodePort
```
> Enable accessing app inside cluster
```bash
ClusterIP
```
> Only private services internal to the cluster
```bash
LoadBalancer
```
> Balance external access (Does not work locally only in cloud provider)

## Getting cluster IP to connect locally
```bash
minikube ip
Or
minikube service SERVICE_NAME --url
```

## Execute all yaml at once
```bash
kubectl create -f FOLDER_CONTAINING_FILES
```