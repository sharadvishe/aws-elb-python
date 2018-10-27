from flask import Flask
import socket

app = Flask(__name__)

@app.route('/hello')
def helloIndex():

    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP")

    return "Host IP:" + host_ip + "            Hostname:" + host_name

if __name__ == '__main__':
	app.run(debug=True)
#app.run(host='0.0.0.0', port= 8088)
