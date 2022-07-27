import socket
from flask import Flask
import mysql.connector


app = Flask(__name__)


mydb = mysql.connector.connect(
  host="lab1_db_1",
  user="aa",
  password="aa"
)


@app.route('/')
def hello():
    hostname = socket.gethostname()
    return 'db: hello'#.format(mydb) # + 'Hello World! I am {}\n'.format(hostname)
