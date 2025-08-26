from flask import Flask, render_template,request
from dotenv import load_dotenv
import os
import pymongo

load_dotenv

MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(os.getenv("MONGO_URI"))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.ItemsDB
collection = db['FormsCollection']

app = Flask(__name__)

@app.route('/')
def welcomePage():
    return render_template('index.html')  

@app.route('/submit', methods=['POST'])
def submitForm():

    Itemname = request.form['Itemname']
    Itemdesc = request.form['Itemdesc']
    
    # Insert the form data into MongoDB
    collection.insert_one({'Itemname': Itemname, 'Itemdesc': Itemdesc})
    
    
    return "Data submitted successfully!" 

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,debug=True)
