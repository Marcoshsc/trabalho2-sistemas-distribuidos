 
from timeit import default_timer as timer
from dateutil import parser
import threading
import datetime
import socket 
import time
  

def startSendingTime(slave_client):
  
    while True:
        slave_client.send(str(
                       datetime.datetime.now()).encode())
  
        print("Tempo recente recebido com sucesso",
                                          end = "\n\n")
        time.sleep(5)
  

def startReceivingTime(slave_client):
  
    while True:

        Synchronized_time = parser.parse(
                          slave_client.recv(1024).decode())
  
        print("Tempo sincronizado no cliente é: " + \
                                    str(Synchronized_time),
                                    end = "\n\n")
  
  

def initiateSlaveClient(port = 8080):
  
    slave_client = socket.socket()          
        

    slave_client.connect(('127.0.0.1', port)) 
  

    print("Começando a receber dados do servidor\n")
    send_time_thread = threading.Thread(
                      target = startSendingTime,
                      args = (slave_client, ))
    send_time_thread.start()
  
  

    print("Começando a receber tempo " + \
                         "sincronizado do servidor.\n")
    receive_time_thread = threading.Thread(
                       target = startReceivingTime,
                       args = (slave_client, ))
    receive_time_thread.start()
  
  

if __name__ == '__main__':
  
    initiateSlaveClient(port = 8080)
