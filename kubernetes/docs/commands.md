# app_1.0
docker build . -t lteixeira93/app-html:1.0
docker login
docker push lteixeira93/app-html:1.0

# app_1.2
docker build . -t lteixeira93/app-html:1.2
docker login
docker push lteixeira93/app-html:1.2

# app_1.3
Nodeport - direct request to specific port instead of loadbalancing between pods
docker build . -t lteixeira93/myapp-php:1.0
docker login
docker push lteixeira93/myapp-php:1.0
# Allow firewall for given port
gcloud compute firewall-rules create myapp-php-service --allow tcp:32481

To run on minikube
minikube service myapp-php-service --url

# Enter in bash to modify app
kubectl exec --stdin --tty myapp-php -- /bin/bash