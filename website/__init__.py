from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = '80fd00af5dec5a001b60e1dc6fb7bd95'


from website import routes