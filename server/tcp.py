import socket

def run_server():
  '''
  Here we are:
  1. Creating a TCP socket
  2. Binding on port 3000 (using localhost)
  3. 
  '''

  tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  tcp_socket.bind(('127.0.0.1', 3000))
  tcp_socket.listen(5)
  tcp_client_connection, address = tcp_socket.accept()
  print('Receiving connection from {}'.format(address))

  while True:
    content = tcp_client_connection.recv(1024)

    if not content:
      break

    content = str(content)
    print('We received from client {} the following: {}'.format(
      address,
      str(content)
    ))

    message = 'The content you send ({}) has {} words'.format(
      str(content),
      len(content.split())
      )
    tcp_client_connection.send(bytes(message, encoding='utf-8'))


run_server()
