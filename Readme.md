Monitor Ram and CPU usage every 3 seconds and sends them to the consumer using 2 different queues

install python
python3 -m pip install pika
sudo pip install --upgrade psutil

sudo docker run -p 9000:15672  -p 1883:1883 -p 5672:5672  cyrilix/rabbitmq-mqtt 
sudo docker run -p 8070:8070 -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp nuclio/dashboard:stable-amd64

python3 send.py
python3 receive.py


