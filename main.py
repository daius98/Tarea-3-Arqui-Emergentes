from flask import Flask, jsonify, request
import controller
from db import create_tables

app = Flask(__name__)

@app.route('/admins', methods=["GET"])
def get_users():
    users = controller.get_users()
    return jsonify(users)

@app.route("/admin", methods=["POST"])
def create_admin():
    admin_details = request.get_json()
    username = admin_details["username"]
    password = admin_details["password"]
    result = controller.create_admin(username, password)
    return jsonify(result)

@app.route("/admin/create_company", methods=["POST"])
def create_company():
    details = request.get_json()
    company_name = details["company_name"]
    result = controller.create_company(company_name)
    return jsonify(result)

@app.route("/admin/create_location", methods=["POST"])
def create_location():
    details = request.get_json()
    company_id = details["company_id"]
    location_name = details["location_name"]
    location_country = details["location_country"]
    location_city = details["location_city"]
    location_meta = details["location_meta"]
    result = controller.create_location(company_id, location_name, location_country, location_city, location_meta)
    return jsonify(result)

@app.route("/admin/create_sensor", methods=["POST"])
def create_sensor():
    details = request.get_json()
    location_id = details["location_id"]
    sensor_name = details["sensor_name"]
    sensor_category = details["sensor_category"]
    sensor_meta = details["sensor_meta"]
    result = controller.create_sensor(location_id, sensor_name, sensor_category, sensor_meta)
    return jsonify(result)

@app.route("/admin/<username>", methods=["GET"])
def get_user(username):
    user = controller.get_user(username)
    return jsonify(user)

@app.route('/company', methods=["GET"])
def get_company():
    users = controller.get_company()
    return jsonify(users)

@app.route('/location/<location_id>', methods=["GET"])
def get_location(location_id):
    location = controller.get_location(location_id)
    return jsonify(location)

@app.route('/locations', methods=["GET"])
def get_locations():
    location = controller.get_locations()
    return jsonify(location)

@app.route("/location", methods=["PUT"])
def update_location():
    details = request.get_json()
    location_id = details["location_id"]
    location_name = details["location_name"]
    location_country = details["location_country"]
    location_city = details["location_city"]
    location_meta = details["location_meta"]
    result = controller.update_location(location_id, location_name, location_country, location_city, location_meta)
    return jsonify(result)

@app.route("/location/<location_id>", methods=["DELETE"])
def delete_location(location_id):
    result = controller.delete_location(location_id)
    return jsonify(result)

@app.route('/sensor/<sensor_id>', methods=["GET"])
def get_sensor(sensor_id):
    sensor = controller.get_sensor(sensor_id)
    return jsonify(sensor)

@app.route('/sensors', methods=["GET"])
def get_sensors():
    sensor = controller.get_sensors()
    return jsonify(sensor)

@app.route("/sensor", methods=["PUT"])
def update_sensor():
    details = request.get_json()
    sensor_id = details["sensor_id"]
    sensor_name = details["sensor_name"]
    sensor_category = details["sensor_category"]
    sensor_meta = details["sensor_meta"]
    result = controller.update_sensor(sensor_id, sensor_name, sensor_category, sensor_meta)
    return jsonify(result)

@app.route("/sensor/<sensor_id>", methods=["DELETE"])
def delete_sensor(sensor_id):
    result = controller.delete_sensor(sensor_id)
    return jsonify(result)

@app.route("/v1/sensor_data", methods=["POST"])
def insert_sensor_data():
    details = request.get_json()
    sensor_apy_key = details["sensor_apy_key"]
    sensor_id = details["sensor_id"]
    variable_name_1 = details["variable_name_1"]
    variable_1 = details["variable_1"]
    variable_name_2 = details["variable_name_2"]
    variable_2 = details["variable_2"]
    result = controller.insert_sensor_data(sensor_apy_key, sensor_id, variable_name_1, variable_1, variable_name_2, variable_2)
    return jsonify(result)

@app.route('/v1/sensor_data/', methods=["GET"])
def get_sensor_data(sensor_id):
    details = request.get_json()
    sensor_apy_key = details["sensor_apy_key"]
    sensor_id = details["sensor_id"]
    time_from = details["time_from"]
    time_to = details["time_to"]
    sensor = controller.get_sensor_data(sensor_apy_key,sensor_id, time_from, time_to)
    return jsonify(sensor)

if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)