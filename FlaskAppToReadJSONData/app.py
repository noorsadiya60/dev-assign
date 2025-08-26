from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome Home"

@app.route('/api')
def studentData():
    file = open('./studentData.json',"r")
    content = file.read()
    return content

if(__name__ == "__main__"):
    app.run(debug=True)