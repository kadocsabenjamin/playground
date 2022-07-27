import socket
from flask import Flask
import mysql.connector


app = Flask(__name__)


mydb = mysql.connector.connect(
  host="localhost",
  user="bb",
  password="ab"
)


@app.route('/')
def hello():
    hostname = socket.gethostname()
    return 'db: {}'.format(mydb) # + 'Hello World! I am {}\n'.format(hostname)
