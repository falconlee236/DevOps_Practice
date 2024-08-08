# minikube 설치하기
## linux
### minikube binary 가져오기
`curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64`
### minikube 설치
`sudo install minikube-linux-amd64 /usr/local/bin/minikube`
### minikube 실행
`minikube start`
이러면 구성파일을 설치한다.
```bash
sangylee@sangylee-ubuntu:~/devOps_practice/boaz-docker$ minikube start
😄  minikube v1.33.1 on Ubuntu 20.04
✨  Automatically selected the docker driver. Other choices: none, ssh
📌  Using Docker driver with root privileges
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.44 ...
💾  Downloading Kubernetes v1.30.0 preload ...
    > preloaded-images-k8s-v18-v1...:  342.90 MiB / 342.90 MiB  100.00% 24.96 M
    > gcr.io/k8s-minikube/kicbase...:  481.58 MiB / 481.58 MiB  100.00% 22.81 M
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🐳  Preparing Kubernetes v1.30.0 on Docker 26.1.1 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
💡  kubectl not found. If you need it, try: 'minikube kubectl -- get pods -A'
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

### dashboard 웹 브라우저 열기
`minikube dashboard --port 3000`
```bash
🤔  Verifying dashboard health ...
🚀  Launching proxy ...
🤔  Verifying proxy health ...
🎉  Opening http://127.0.0.1:3000/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...
^C
```

# kubectl
쿠버네티스에 명령어를 내리기 위해서는 kubectl이 필요하다
## linux
### 바이너리 파일 설치
`curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"`
### kubectl 설치
`sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl`
### 설치 확인
```bash
sangylee@sangylee-ubuntu:~/devOps_practice/boaz-docker$ kubectl version --client
Client Version: v1.30.3
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
sangylee@sangylee-ubuntu:~/devOps_practice/boaz-docker$ kubectl get nodes
NAME       STATUS   ROLES           AGE     VERSION
minikube   Ready    control-plane   4m56s   v1.30.0
sangylee@sangylee-ubuntu:~/devOps_practice/boaz-docker$ kubectl get pods -A
NAMESPACE     NAME                               READY   STATUS    RESTARTS        AGE
kube-system   coredns-7db6d8ff4d-v4qhr           1/1     Running   0               4m52s
kube-system   etcd-minikube                      1/1     Running   0               5m8s
kube-system   kube-apiserver-minikube            1/1     Running   0               5m6s
kube-system   kube-controller-manager-minikube   1/1     Running   0               5m9s
kube-system   kube-proxy-6b6hg                   1/1     Running   0               4m52s
kube-system   kube-scheduler-minikube            1/1     Running   0               5m6s
kube-system   storage-provisioner                1/1     Running   1 (4m20s ago)   5m4s
```