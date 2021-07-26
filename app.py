from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'Contact': 2832023898,
        'Name': 'Anonymous 1',
        'done': False
    },
    {
        'id': 2,
        'Contact': 3943134989,
        'Name': 'Anonymous 2',
        'done': False
    }
]

@app.route('/add-data', methods = ["POST"])

def add_contacts():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        }, 400)
    
    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "Contact Added Successfully!"
    })

@app.route('/get-data')

def get_contacts():
    return jsonify({
        "data": contacts
    })

if (__name__ == "__main__"):
    app.run(debug = True)