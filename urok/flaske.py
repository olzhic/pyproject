from flask import Flask

app = Flask(__name__)

@app.route('/poshel_nahui/')
def hello():
    return 'hello world from flask poshel nahui'

app.run()