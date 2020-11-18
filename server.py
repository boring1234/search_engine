from flask import Flask, redirect, url_for, request, render_template
from retriver import retrive
import json
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def prompt():
    if request.method == 'POST':
        user_input = request.form['nm']
        results = generate_results(retrive(user_input))
        return render_template('result.html', output=results)#page with results
    else:
        return render_template('entry.html')#empty page that prompt user input

def generate_results(result_ls):
    output = []
    with open('./WEBPAGES_RAW/bookkeeping.json', mode='r') as f:
        url_dict = json.load(f)
        for tup in result_ls:
            url = url_dict[tup[0]]
            output.append('%s\t%s' % (tup[0], url))
    return output

if __name__ == '__main__':
    app.run(debug = True)
    #export FLASK_APP=server.py
    #python -m flask run
