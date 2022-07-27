from flask import Flask
import mysql.connector


app = Flask(__name__)


mydb = mysql.connector.connect(
  host="mysql",
  user="aa",
  password="aa"
)


@app.route('/')
def hello():
    hostname = socket.gethostname()
    return 'db: hello'#.format(mydb) # + 'Hello World! I am {}\n'.format(hostname)
