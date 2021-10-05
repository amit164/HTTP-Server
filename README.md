# HTTP-Server
1. [Introduction](#introduction)  
2. [Dependencies](#dependencies)
3. [Installation](#installation)

dgf
## Introduction
A python implementaion to HTTP-server (with a browser as a client). The client sends (as HTTP-1.1 request) to the server the name of the file he wants to download from the _files_ folder. If the file is in a sub-folder, it's name has to include a path. The server does not provide a parallel connections and therefor there is a maximum time (set to 1 sec) that the server waits for a request.

* When the client sends ```/``` as file name, the server will return the ```index.html``` file.
* When the client sends ```redirect.http```, the server will return the status _301 Moved Permanently_ and the path ```/result.html```.
* When the client sends a path that does not exist, the server will return the status _404 Not Found_ and close the connection. 


## Dependencies:
* MacOS / Linux with python
* Web browser

## Installation:
1. Clone the repository:  
    ```
    $ git clone https://github.com/amit164/HTTP-Server.git
    ```
2. Run the server with the command:
    ```
    $ python3 server.py 8080
    ```
    Note: '8080' is the port so you can use any port you want.
3. Open your web browser (Chrome for expamle) and as URL, type the path of the file you want to download from the _files_ folder. For instance:
    ```
    $ localhost:8080/a/oh_no.jpg
    ```
    Note: If you are running the server and client in different computers, you will have to write the server IP instead of the term ```localhost```.

