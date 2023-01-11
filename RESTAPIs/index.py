from flask import Flask, request, jsonify
import json

app = Flask(__name__)

countries = [
    {"id": '1', "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": '2', "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": '3', "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

# Find data in json
def _find_next_id(id):
    data = [x for x in countries if x["id"]==id]
    return data

# GET RESTAPIs
@app.route('/country', methods=["GET"])
def get_country():
    return jsonify(countries)

#Get by ID
@app.route('/country/<id>', methods=["GET"])
def get_country_id(id):
    data = [x for x in countries if x["id"]==id]
    return jsonify(data)

#POST RESTAPIs
@app.route('/country', methods=["POST"])
def add_country():
    id = request.form.get('id')
    name = request.form.get('name')
    capital = request.form.get('capital')
    area = request.form.get('area')

    data = {
        "id": id, 
        "name": name, 
        "capital": capital, 
        "area": area
        }

    if (_find_next_id(id)):
        return {"error": "Bad Request"}, 400
    else:
        countries.append(data)
        return jsonify(countries)

# Code Here for PUT APIs
@app.route('/country', methods=["PUT"])
def update_country():
    global countries

    id = str(request.args.get('id'))
    name = request.args.get('name')
    capital = request.args.get('capital')
    area = str(request.args.get('area'))

    update_data = {
        "id": id, 
        "name": name, 
        "capital": capital, 
        "area": area
        }

    if (_find_next_id(id)):
        data = [x for x in countries if x["id"]!=id]
        data.append(update_data)
        countries = data
        return jsonify(countries)
    else:
        return {"error": "Bad Request ID = " + id}, 400

#Delete REST APIs
@app.route('/country', methods=["DELETE"])
def del_country():
    id = request.args.get('id')
    data = [x for x in countries if x["id"]!=id]
    return jsonify(data), 201

@app.errorhandler(404)
def page_not_found(e):
    return {"error": "File not found"}, 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True) #127.0.0.1