# TCP Client-Server Model 

A simple TCP server and tcp client for learning some network programming stuff.


![client-server-model](https://phoenix.goucher.edu/~kelliher/cs43/clientserver.gif)


It uses Python native socket API, so you need to install Python in order to run this project.


## TCP Server

It binds port 3000 by default.

For this, run: 

```bash
python server/tcp.py
```


## TCP Client


```bash
python client/tcp.py
```

## Important concepts before getting started

### Network Sockets

  Endpoint to send/receive data from network and allows communication between two computers. It must have an IP address along with a port.

### Port

  Allow different processes/applications from same host to share network resources.

For more details:

http://www.steves-internet-guide.com/tcpip-ports-sockets/
