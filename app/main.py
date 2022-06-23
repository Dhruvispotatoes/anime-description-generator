"""
    Bonus points if you want to have internship at AI Camp
    1. How can we save what user built? And if we can save them, like allow them to publish, can we load the saved results back on the home page?
    2. Can you add a button for each generated item at the frontend to just allow that item to be added to the story that the user is building?
    3. What other features you'd like to develop to help AI write better with a user?
    4. How to speed up the model run? Quantize the model? Using a GPU to run the model?
"""

import os

from flask import Flask, escape, request, redirect, url_for, render_template, session
from utils import get_base_url

from aitextgen import aitextgen

ai = aitextgen(model_folder="model1/", to_gpu=False)

port = 65421
base_url = get_base_url(port)

if base_url == '/':
    app = Flask(__name__)
else:
    app = Flask(__name__, static_url_path=base_url+'static')

app.secret_key = os.urandom(64)

@app.route(f'{base_url}')
def home():
    return render_template('index.html')

@app.route(f'{base_url}/try', methods=['GET', 'POST'])
def try_():
    prompt = ''
    amount = 1
    temperature = 0.9
    output = ['Your description will appear here.']

    if request.method == 'POST':
        prompt = request.form['prompt']

        if 'amount' in request.form:
            amount = int(request.form['amount'])
            if amount > 5:
                amount = 5
            elif amount < 1:
                amount = 1

        if 'temperature' in request.form:
            temperature = float(request.form['temperature'])
            if temperature < 0.05:
                temperature = 0.05

        output = ai.generate(
            n=amount,
            batch_size=1,
            prompt=str(prompt),
            max_length=300,
            temperature=temperature,
            return_as_list=True
        )

    return render_template(
        'try.html',
        prompt=escape(prompt),
        amount=amount,
        temperature=temperature,
        output=map(escape, output)
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    website_url = 'cocalc9.ai-camp.dev'
    print(f'Try to open\n\n    https://{website_url}{base_url}\n\n')
    app.run(host='0.0.0.0', port=port, debug=True)
