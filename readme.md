https://www.youtube.com/watch?v=UC2wj3Bg3eM&list=PLqndseDs9rmIwtzB1i08UWkQjQhpmZhtH
there are 2 api's in playwright 
1. sync -> it works as normal python code
2. async ->  it uses the async and wait keyword to control flow of execution.
pip install pytest-playwright







EKS in AWS:
------------
As EKS is paid we can do same in kind please follow steps below
1. Do aws --configure
access key 
AKIAW4MD2UWPKBHWL7S3
secrity key
ZeQmQh5thMJElPg8l4Cr+8ICmpmpujZK8P07Dxvq
ap-south-1
aws configure
2. Now create ECR repo in AWS then push the image into ECR aws
aws ecr create-repository --repository-name playwright-tests
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 473259746718.dkr.ecr.ap-south-1.amazonaws.com
docker tag playwright_python:latest <account-id>.dkr.ecr.<region>.amazonaws.com/playwright-tests:latest
docker tag playwright_python:latest 473259746718.dkr.ecr.ap-south-1.amazonaws.com/playwright-tests:latest
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/playwright-tests:latest
docker push 473259746718.dkr.ecr.ap-south-1.amazonaws.com/playwright-tests:latest

3. Install kind in windows
curl.exe -Lo kind-windows-amd64.exe https://kind.sigs.k8s.io/dl/v0.30.0/kind-windows-amd64 Move-Item .\kind-windows-amd64.exe C:\Program Files\kind.exe

4. Once image is in ecr and kind is installed we need to write a yaml file to create pod.
Kubernetes needs credentials to pull images from a private registry (ECR). You can do this with a secret called imagePullSecrets.
kubectl create secret docker-registry ecr-creds ^
  --docker-server=473259746718.dkr.ecr.ap-south-1.amazonaws.com ^
  --docker-username=AWS ^
  --docker-password="%AWS_ECR_PASS%"
secreate key is
eyJwYXlsb2FkIjoiV0s5QVY0ZzlFbGw4NzFzZzhCV3Vaa3czVUQ0bzR5YkRuMGN5dDNrbGw4bDJxTWJSaktjUU9OZTRPdGZNOTNmRkw2eE01Z3ZiZkh2eEJsMkJUWnJxODMzZi9OaEhWZ211K09WcjhNNnU5WUJFcW8zRUV3UlBzVzhpa1Q4dEVTZzhDNTNHWSt3dWUrTGU2ck0wajliTURvYUdRUk9kZm9xc3VERVpaWlUrdXJZWDh4bVRhYnBuNEdoa2ZsSXB2cG0yeHFhUmhPMlVYaEQzaEIya0Y1WHlrVUxoZmZuckpSbldQSlVFNkdwTnRPSnFDTHBIaDNpSDBLVnhwS3JSdXhxbUZoLzRNa1FaVGpGWjMzVFUwTVkwcy9uUzR5NU5IRysyS0V0TWRaWHB3YzVMT05BakdIa1lrckpTTGlIalIyYWpUeU82Vm9vek04OTU4VFdtY1VkWCtLcS9HZnZ6RFNGWGZMdjliOGNYeG5DL2h6bm0wRWdNd0dYa0pUT2VXa2d1YTBObGZ6QmxMMGU0WkxXZHhKcm1DTGU1S1YreUJscGRhaGxIWDNtWEhLaEQ4S0hFWVZIQjEraDBZR25YVzFmc0ZwRUFVSjZHWE9jS1JGaTFCMGlNbEZtRWsvV1NZcVZabFlPQktRSEVFU1F6eUxXR1FnY0UyQ3FQZGJJbzRDN3UxdXQwMG1GMkxLOHpYWEtzNFYxaUVlYk55eWNjb2JTejg1S3NkRmE4cGJWYWVYdkVGVkRoNkpqY1ptYkoxeTUyOGRYV0dZaTNhNWgvdnhSeXZubXFJeTV4L2ZtQ1hHbGxaNzd5M0NhYkdmVHpWVFZzMlcwNEN3d29qeGk5amhNbEhxMFpnZ1M4QXR6RXRjVmVCeEIzQVVBZXVoWnhrTy9BeEJRUTd5RDdLem13Y0hwMS9XVnloY1NVdDB5eVQ2WE9sVnVrR2l6enlYSnYxOHlNa0dpcHNHSTVxTzZxYW85ZFM4RmVGQlNFenNpQVN3RkRuSWRxOUR3MzlGb2ljMi9wV0FYTmh0eFhsbmhyNGkyMlZ1YTdWKzViczVUNCs5UGxKRjhpVlM0TGtrWXdhQi9PcmtIZmgrMXd0YVhYbUxDT3RUK0cxNGZkS2hUbzluMEdZbGVTYWJ6U2QvdmZ3UHdnMWtiWnNpL05RNWJOU0N5RjJKbVFZb0RjdHFVNVg4YlA1a3RvRFo2b2tCY25tQ2dqYWcrc2JHM0crQ1MxOGd5OGZXUHNyRE0wT3BiWW9jOVJtUFBzeHdtVGNFcXZHV0p6V2dSNVlOSWpmNmpwajN1LzBMWVN1TjNoQnIrcWF0aFh2OEFjTCtHRHhOeUtxblNha0tmVG8zTzVLMzhqejI5NWR6V0QxWHN1QXdVM0l0V0t5dz09IiwiZGF0YWtleSI6IkFRSUJBSGlIV2FZVG5SVVdDYm56KzdMdk1HK0FQdlRIekhsQlVROUZxRW1WMjZCZHd3SDljUnI5TnBNcHlVaW9hdzgyMThTakFBQUFmakI4QmdrcWhraUc5dzBCQndhZ2J6QnRBZ0VBTUdnR0NTcUdTSWIzRFFFSEFUQWVCZ2xnaGtnQlpRTUVBUzR3RVFRTU1vQ3BlWHo0SDhkcElTbXdBZ0VRZ0R0NTBFSWV0QUFmeVo4TW5qN2JEOWhqN2gwK2hmQnhUUDBMN2N1N2VZeEI0NktrYzNKU3dGTVRWUjE2NWVnOWYxNjFPWU5OTE1lQU1NSkpxZz09IiwidmVyc2lvbiI6IjIiLCJ0eXBlIjoiREFUQV9LRVkiLCJleHBpcmF0aW9uIjoxNzU5Njk3MzUyfQ=

now create yanl file and do 
kubectl apply -f playwright-deployment.yaml
here we used to write pull image from the ecr 
As i m running playwright-deployment.yaml in local and docker image in ECR can't push this 

5. So manually load image into cluster using 
kind load docker-image 473259746718.dkr.ecr.ap-south-1.amazonaws.com/playwright-tests:latest --name test-cluster

6. once it is done use 
kubectl apply -f playwright-deployment.yaml
to check test passed or not
kubectl logs test-image _> test image is pod name 
