from flask import Flask
from flask import request
from flask import Response
import json

from vowel_counter import count_vowels

app = Flask(__name__)

@app.route('/')
def vowelcount(): #needs error handling
    if request.args.get('x'):
        string = str(request.args.get('x'))
        num_of_vowels = str(count_vowels(string))
        
        r = {
            "String" : string,
            "Vowels" : num_of_vowels
        }
    
    else:
        r = {
            "String" : "No String entered",
            "Vowels" : "N/A"
        }

    
    reply = json.dumps(r)

    response = Response(response = reply, status = 200, mimetype="application/json")

    response.headers['Content-Type']='application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    


    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)