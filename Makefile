.PHONY: test clean teste2e build

build:
	docker build -t app app/

deploy:
	kubectl apply -f templates/kinesis.service.yaml
	kubectl apply -f templates/localstack.deployment.yaml
	kubectl apply -f templates/s3.service.yaml
	kubectl apply -f templates/app.deployment.yaml

clean:
	kubectl delete -f templates/kinesis.service.yaml
	kubectl delete -f templates/localstack.deployment.yaml
	kubectl delete -f templates/s3.service.yaml
	kubectl delete -f templates/app.deployment.yaml

localstack:
	docker-compose up
