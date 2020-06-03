from flask import Flask
import config
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
# Use a service account
cred = credentials.Certificate(config.key)
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/rides',methods=['GET'])
def get_rides():
    #Getting all documents and ordering them by day
    query = db.collection("rides").order_by("day")
    docs = query.stream()
    result = []

    #Adding all documents to a list
    for doc in docs:
        result.append(doc.to_dict())

    #Creating json out of that list and returning it
    return jsonify(result)

if __name__ == '__main__':
    app.run()
