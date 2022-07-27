import socket
from flask import Flask
import mysql.connector


app = Flask(__name__)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aa"
)


@app.route('/')
def hello():
    hostname = socket.gethostname()
    return 'Hello World! I am {}\n'.format(hostname)