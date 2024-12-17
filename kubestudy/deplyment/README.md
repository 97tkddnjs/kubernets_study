
참고 자료
https://kubernetes.io/ko/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/#kustomization-yaml-%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0

https://freedeveloper.tistory.com/430


전체 실행 명령어

 kubectl apply -k ./



1차 실습 

 scale 증가 3개 pods 로
 kubectl scale deployment wordpress --replicas=3


 위험 초기화 명령어

 kubectl delete all --all

 kubectl delete pvc mysql-pv-claim

 kubectl delete pvc wp-pv-claim