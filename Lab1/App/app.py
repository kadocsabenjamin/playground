import socket
from flask import Flask

from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'lab1_db_1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'



@app.route('/')
def hello():
    hostname = socket.gethostname()
    return 'db: {}'.format(mydb) # + 'Hello World! I am {}\n'.format(hostname)
