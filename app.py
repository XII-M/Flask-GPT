from flask import Flask, render_template, jsonify, request
import config
import openai
import aiapi
from langchain.memory import ConversationSummaryBufferMemory
from langchain.llms import OpenAI
import json


def page_not_found(e):
    return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)

messages = []

llm = OpenAI()

@app.route('/', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':
        prompt = request.form['prompt']

        print(prompt)
        print("Here")

        answer = aiapi.chatResponse(prompt)

        res = {}
        res['answer'] = answer

        return jsonify(res), 200


    return render_template('index.html', **locals())


@app.route('/processUserInfo/<prompt>', methods=['POST'])
def processUserInfo(prompt):

    print(prompt)
    print("-------------------------")

    userInfo = json.loads(prompt)
    

    print(userInfo["prompt"])

    answer = aiapi.chatResponse(userInfo['prompt'])
   
    return answer

if __name__ == '__main__':
    
    app.run()
