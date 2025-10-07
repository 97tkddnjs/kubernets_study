# Kubernetes Multi-Ingress Test

Docker Desktop의 Kubernetes 환경에서 여러 Ingress 리소스를 테스트하는 프로젝트입니다.

## 사전 요구사항

- Docker Desktop with Kubernetes enabled
- kubectl CLI tool

## NGINX Ingress Controller 설치

Docker Desktop의 Kubernetes는 기본적으로 Ingress Controller를 포함하지 않습니다. 따라서 별도 설치가 필요합니다.

1. NGINX Ingress Controller 설치
docker desktop 오른쪽 상단 메뉴에서 Kubernetes 탭으로 이동

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml

kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/name=ingress-nginx \
  --timeout=90s
```

## 로컬 호스트 설정

/etc/hosts 파일에 테스트용 도메인을 추가합니다:

```bash
# MacOS의 경우
sudo vi /etc/hosts

# 다음 라인 추가
127.0.0.1 localhost a.example.com b.example.com c.example.com d.example.com e.example.com f.example.com
```

## 리소스 배포

1. 첫 번째 그룹 (a,b,c 도메인) 배포:
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f kube1.yaml
```

2. 두 번째 그룹 (d,e,f 도메인) 배포:
```bash
kubectl apply -f kube2.yaml
```

## 작동 원리

- 모든 Ingress 리소스는 동일한 NGINX Ingress Controller를 사용합니다 (`kubernetes.io/ingress.class: "nginx"`).
- 중요 도메인(a,b,c)과 일반 도메인(d,e,f)을 별도의 Ingress 리소스로 분리하여 관리합니다.
- 하나의 Controller로 여러 Ingress 리소스를 관리할 수 있어 안전하게 도메인을 추가/수정할 수 있습니다.

## 상태 확인

```bash
# Ingress Controller 상태 확인
kubectl get pods -n ingress-nginx

# Ingress 리소스 확인
kubectl get ingress

# 서비스 및 파드 상태 확인
kubectl get svc
kubectl get pods
```

## 테스트

브라우저에서 다음 URL에 접속하여 테스트할 수 있습니다:
- http://a.example.com
- http://b.example.com
- http://c.example.com
- http://d.example.com
- http://e.example.com
- http://f.example.com

## 주의사항

- HTTPS를 사용하는 경우 별도의 TLS 인증서 설정이 필요합니다.
- 테스트 환경이므로 실제 프로덕션 환경에서는 적절한 보안 설정이 추가로 필요합니다.

## 리소스 삭제

```bash
# Ingress 리소스 삭제
kubectl delete -f kube1.yaml
kubectl delete -f kube2.yaml

# Service와 Deployment 삭제
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml

# NGINX Ingress Controller 삭제
kubectl delete -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml
```

모든 리소스가 제대로 삭제되었는지 확인:
```language=bash
# 각 리소스 타입별 확인
kubectl get ingress
kubectl get service
kubectl get deployment
kubectl get pods
kubectl get pods -n ingress-nginx
```

추가로 /etc/hosts 파일에서 테스트용으로 추가했던 도메인들도 제거하시면 됩니다:
```language=bash
sudo vi /etc/hosts
# a.example.com, b.example.com, c.example.com, d.example.com, e.example.com, f.example.com 항목 제거
```
```




