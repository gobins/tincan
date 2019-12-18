# Exercise

## Pre-requisites
* Docker needs to be installed on your local machine
* minikube to test the deployment into k8 cluster
* docker-compose to stand up localstack
* python 2.7 installed on your machine

## Project structure
The repo contains the following files:
* app - contains python scripts for calling ec2, kinesis and s3
* templates - contains kube templates to deploy localstack
* docker-compose.yaml - use this to stand up a localstack on your machine

## Exercise 1
* Stand up localstack
    ```
    make localstack
    ```
* Install requirements
    ```
    pip install -r app/requirements.txt
    ```
* Creating kinesis stream
    ```
    python app/kinesis.py
    ```
* Creating s3 bucket
    ```
    python app/s3.py
    ```

### Deploy into minikube
* Run the following command to deploy into a kube cluster
    ```
    make deploy
    ```

## Exercise 2
* Before running the test, make sure you can your local aws config setup
   To roll an autoscaling group, run the script with inputs
   ```
   python asg.py 
   ``` 


## Things to improve
* Although the app and localstack gets deploy into the cluster, the app testing is still not functional.
* Firehose to s3 still to be implemented
* Testing has not been done for exercise 2 due to not having access to a AWS environment.

