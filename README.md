# Instruction to run the project 
<ol>
<li>in the main directory Run `Vagrant up`</li>
<li>```vagrant ssh```</li>
<li>```sudo cat /etc/rancher/k3s/k3s.yaml``` and copy the file</li>
<li>Go to ~/.kube/config and paste the file</li>
<li>Run ```kubectl apply -f deployment/```</li>
<li>run the script.sh that in all microservices folders to create and seed the database</li>
<li>OR do this  
```kubectl exec -it <pod_NAME(If "person the name will person-postgresy5r5yruygjh for example")> -- bash```
``` vi init_connection_db.sql```
``` psql -U ct_admin -d connection -f init_connection_db.sql```
 `</li>
<li>the project on port `localhost:30000`</li>
</ol>
