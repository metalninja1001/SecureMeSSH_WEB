![image](https://user-images.githubusercontent.com/101802030/235102104-77fedde1-060f-4252-b42b-72827b828679.png)





## SecureMeSSH_WEB
This is the web app version of the securemessh python3 application. The client can now be run in your web browser of choice.

## How to:
- Ensure that you have python installed on the device you would like to run the client on. You may do so by following this link : https://www.python.org/downloads/
- Clone the repo. Run - `sudo git clone https://github.com/metalninja1001/SecureMeSSH_WEB.git` in your terminal.
- Modules(dependencies) - `paramiko`, `typer`
- To start the client. Run - `sudo python3 securemessh.py`

-- You may then open your web browser of choice, and navigate to `http://127.0.0.1:5000`. You should see the following screen :

![image](https://user-images.githubusercontent.com/101802030/235178867-31b00a9c-23c1-4416-9084-2bce7ef817ab.png)




- You will need to enter the server name and/or ip address, username, password and a message.

### To receive a message. Start a listener on another device running bash. This device could be on your local lan or the internet.
- A listener may be started using the following command : `sudo nc -l -p 443 -k`

![image](https://user-images.githubusercontent.com/101802030/235178175-57d3ba18-a6cf-42d4-a562-c0ad9f3daefc.png)

