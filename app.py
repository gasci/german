from flask import Flask, jsonify, request, render_template, redirect
import json
from flask_classful import FlaskView
from dotenv import load_dotenv
import os

app = Flask(__name__, template_folder='templates')

# HOME = os.environ['CLUSTER_USERNAME']
# CLUSTER_PASSWORD = os.environ['CLUSTER_USERNAME']

# print(HOME)
# print(CLUSTER_PASSWORD)

@app.route("/")
def starting_url():
    return redirect("/word")

class WordView(FlaskView):
    def __init__(self):
        with open("assets/vocab.json", "r", encoding="utf-8") as json_file:
            self.data = json.load(json_file)

        # load variables
        load_dotenv(".env")
        # app config
        app.config['JSON_AS_ASCII'] = False
    
    def index(self):

        words = self.data.keys()

        return render_template('main.html', words=words) #

    def search(self):
        word = request.args.get("word")
        
        # increase the request count by one
        # self.data[word]["request_count"] += 1

        # print(self.data)

        # with open("assets/vocab.json", "w", encoding="utf-8") as jsonFile:
        #     json.dump(self.data, jsonFile, ensure_ascii=False)
        response = self.data[word]

        
        return render_template('word.html', **response) 

        #return jsonify(response=response)

WordView.register(app)

if __name__ == "__main__":
  app.run(host='0.0.0.0')