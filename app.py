import firebase_admin
import config
from flask import Flask
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)

# Use a service account
cred = credentials.Certificate(config.key)
firebase_admin.initialize_app(cred)

db = firestore.client()



@app.route('/')
def hello_world():
    users_ref = db.collection(u'rides')
    docs = users_ref.stream()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))


    return "Request completed"


if __name__ == '__main__':
    app.run()
