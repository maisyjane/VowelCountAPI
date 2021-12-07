from flask import Flask
from flask import request
from flask import Response
from flask import abort
import json
from werkzeug.exceptions import HTTPException, abort

from vowel_counter import count_vowels

app = Flask(__name__)

isDigit = False

@app.route('/')
def vowelcount(): 
    if not request.args.get('x'):
        global isDigit
        isDigit = False
        abort(404)

    if request.args.get('x'):
        string = str(request.args.get('x'))
        
        if string.isdigit():
            isDigit = True
            abort(404)
        else:
            num_of_vowels = str(count_vowels(string))
            r = {
                "String" : string,
                "answer" : num_of_vowels,
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
    if isDigit:
        error_text = "Please enter character strings, not numbers"
    else:
        error_text = "No Text Entered"
    r = {
                "String" : error_text,
                "answer" : 0,
                "Status Code" : "404",
                "Errors" : "true"
        }
    status = 404
    reply = json.dumps(r)
    response = Response(response = reply, status = status, mimetype="application/json")
    response.headers['Content-Type']='application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

#500 error?




if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug= True)