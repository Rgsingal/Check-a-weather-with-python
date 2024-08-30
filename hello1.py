from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
     return "hello Universe"
print ("I am loving to make programs in python language.")
