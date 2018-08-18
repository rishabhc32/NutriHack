from flask import Flask
from werkzeug import FileStorage
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/nutrihack_api', methods=['POST','GET'])
def nutrihack_api():
    FileStorage(stream=request.files['nutrient_info']).save('testpic.jpg')
    resp = Response('Hello World')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
