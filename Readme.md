# Serverless Computing Project

In IoT, in some cases, we need to monitor available devices in case of resource utilization.
This simple IoT project, monitors RAM and CPU usage every 3 seconds and sends them to the consumer using 2 different queues (one for RAM and one for CPU).

# Requirements

- Ubuntu 20.04
- Docker and Docker Compose 
- Nuclio
- RabbitMQ
- Python

# Installation
1. installing python
```
sudo apt install -y python3-pip
```
5. Installing required libraries (pika and psutil)
``` 
python3 -m pip install pika 
sudo pip install --upgrade psutil
````
3. Running docker containers of RabitMQ and Nuclio
``` 
sudo docker run -p 9000:15672  -p 1883:1883 -p 5672:5672  cyrilix/rabbitmq-mqtt 

sudo docker run -p 8070:8070 -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp nuclio/dashboard:stable-amd64
```
4. Running Sender and Receiver functions
```
python3 send.py
python3 receive.py
```

