import socket
from flask import Flask
import mysql.connector


app = Flask(__name__)


mydb = mysql.connector.connect(
  host="lab1_db_1",
  user="bb",
  password="ab"
)


@app.route('/')
def hello():
    hostname = socket.gethostname()
    return 'db: {}'.format(mydb) # + 'Hello World! I am {}\n'.format(hostname)
