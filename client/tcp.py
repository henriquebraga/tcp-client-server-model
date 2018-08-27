import socket

def run_client():
  '''
  Here we are:
  1. Creating a TCP socket
  '''

  tcp_socket = socket.socket()
  tcp_socket.connect(('127.0.0.1', 3000))
  content = ''

  while content not in ('q', 'Q'):
      content = input('Say something to Server or type or [Q] to exit')
      tcp_socket.send(bytes(content, encoding='utf-8'))
      received_data = tcp_socket.recv(1024)
      print(received_data)

run_client()