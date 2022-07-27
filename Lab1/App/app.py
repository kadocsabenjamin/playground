from flask import Flask
import mysql.connector


app = Flask(__name__)


mydb = mysql.connector.connect(
  host="db",
  user="aa",
  password="aa"
)


@app.route('/')
def hello():
    return 'db: hello'#.format(mydb) # + 'Hello World! I am {}\n'.format(hostname)
