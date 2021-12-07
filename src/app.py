from flask import Flask
from flask import request
from flask import Response
from flask import abort
import json
from werkzeug.exceptions import HTTPException, abort

from vowel_counter import count_vowels

app = Flask(__name__)


@app.route('/')
def vowelcount(): 
    if not request.args.get('x'):
        abort(404)

    if request.args.get('x'):
        string = str(request.args.get('x'))
        
        
        if string.isdigit():
            r = {
                "String" : "Please enter character strings, not numbers",
                "Answer" : "N/A",
                "Status Code" : "400",
                "Errors" : "false"
            }
            status = 400
        else:
            num_of_vowels = str(count_vowels(string))
            r = {
                "String" : string,
                "Answer" : num_of_vowels,
                "Status Code" : "200",
                "Errors" : "false"
            }
            status = 200
            
    reply = json.dumps(r)
    response = Response(response = reply, status = status, mimetype="application/json")

    response.headers['Content-Type']='application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.errorhandler(404)
def route_error_handling(error):
    r = {
                "String" : "No Text Entered",
                "Answer" : 0,
                "Status Code" : "404",
                "Errors" : "true"
        }
    status = 404
    reply = json.dumps(r)
    response = Response(response = reply, status = status, mimetype="application/json")
    response.headers['Content-Type']='application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug= True)