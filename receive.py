#!/usr/bin/env python
import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='cpuusage')
    channel.queue_declare(queue='ramusage')

    def callback(ch, method, properties, body):
        print(" [x] CPU Usage (percentage): %r" % body.decode())
   
    channel.basic_consume(queue='cpuusage', on_message_callback=callback, auto_ack=True)
    
    def callback(ch, method, properties, body):
        print(" [x] RAM Usage (percentage): %r" % body.decode())
        
    channel.basic_consume(queue='ramusage', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for statistics from remote. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
