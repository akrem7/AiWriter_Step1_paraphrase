from flask import Flask, request, render_template
from models.model import gpt2_paraphraser, t5_paraphraser

app = Flask(__name__)

@app.route('/',methods=['POST',"GET"])
def index():
    if request.method=='POST':
        data = request.get_json()
        #generate & return paraphrase using the choosen paraphrase model.
        if data["model"] == "GPT2":
            output = gpt2_paraphraser(data["text"])
        else :
            output = t5_paraphraser(data["text"])
        response = {"text":output}
        return response
    else:
        return render_template("index.html")

#run the server
if __name__== "__main__":
    app.run(debug=True,host='0.0.0.0')