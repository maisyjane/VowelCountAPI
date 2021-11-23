from flask import Flask
from flask import request
from flask import Response

from vowel_counter import count_vowels

app = Flask(__name__)

@app.route('/')
def vowelcount(): #needs error handling
    string = str(request.args.get('x'))
    num_of_vowels = str(count_vowels(string))
    return num_of_vowels


if __name__ == '__main__':
    app.run(port = 5000)