![image](https://user-images.githubusercontent.com/101802030/235101976-79318ec2-bb2d-4644-8030-fa075750c882.png)




## SecureMeSSH_WEB
This is the web app version of the securemessh program. The client can now be run in your web browser of choice.

## How to:
- Ensure that you have python installed on the device you would like to run the client on. You may do so by following the this link : https://www.python.org/downloads/
- Clone the repo. Run - `sudo git clone https://github.com/metalninja1001/SecureMeSSH_WEB.git` in your terminal.
- To start the client. Run - `sudo python3 securemessh.py`

-- You may then open your web browser of choice, and navigate to `http://127.0.0.1:5000`. You should see the following screen :

![image](https://user-images.githubusercontent.com/101802030/234892099-a0fee48f-f6fe-42ce-8808-80adaaa407c6.png)



- You will need to enter the server name and/or ip address, username, password and a message.

### To receive a message. Start a listener on another device running bash. This device could be on your local lan or the internet.
- A listener may be started using the following command : `sudo nc -l -p 443 -k`
