from db import get_db
import uuid, time

def create_admin(username, password):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO Admin(username, password) VALUES (?, ?)"
    cursor.execute(statement, [username, password])
    db.commit()
    return True

def create_company(company_name):
    db = get_db()
    cursor = db.cursor()
    company_apy_key = str(uuid.uuid4())
    statement = "INSERT INTO Company(company_name, company_apy_key) VALUES (?, ?)"
    cursor.execute(statement, [company_name, company_apy_key])
    db.commit()
    return True

def create_location(company_id, location_name, location_country, location_city, location_meta):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO Location(company_id, location_name, location_country, location_city, location_meta) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [company_id, location_name, location_country, location_city, location_meta])
    db.commit()
    return True

def create_sensor(location_id, sensor_name, sensor_category, sensor_meta):
    db = get_db()
    cursor = db.cursor()
    sensor_apy_key = str(uuid.uuid4())
    statement = "INSERT INTO Sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_apy_key) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [location_id, sensor_name, sensor_category, sensor_meta, sensor_apy_key])
    db.commit()
    return True

def get_user(username):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT username FROM Admin WHERE username = ?"
    cursor.execute(statement, [username])
    return cursor.fetchone()

def get_users():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Admin"
    cursor.execute(query)
    return cursor.fetchall()

def get_company():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Company"
    cursor.execute(query)
    return cursor.fetchall()

def get_location(location_id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM Location WHERE location_id = ?"
    cursor.execute(statement, [location_id])
    return cursor.fetchone()

def get_locations():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Location"
    cursor.execute(query)
    return cursor.fetchall()

def update_location(location_id, location_name, location_country, location_city, location_meta):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE Location SET location_name = ?,location_name = ?, location_country = ?, location_city = ?, location_meta = ? WHERE location_id = ?"
    cursor.execute(statement, [location_name, location_country, location_city, location_meta, location_id])
    db.commit()
    return True

def delete_location(location_id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM Location WHERE location_id = ?"
    cursor.execute(statement, [location_id])
    db.commit()
    return True

def get_sensor(sensor_id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM Sensor WHERE sensor_id = ?"
    cursor.execute(statement, [sensor_id])
    return cursor.fetchone()

def get_sensors():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Sensor"
    cursor.execute(query)
    return cursor.fetchall()

def update_sensor(sensor_id, sensor_name, sensor_category, sensor_meta):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE Sensor SET sensor_name = ?, sensor_category = ?, sensor_meta = ? WHERE sensor_id = ?"
    cursor.execute(statement, [sensor_name, sensor_category, sensor_meta, sensor_id])
    db.commit()
    return True

def delete_sensor(sensor_id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM Sensor WHERE sensor_id = ?"
    cursor.execute(statement, [sensor_id])
    db.commit()
    return True

def insert_sensor_data(sensor_apy_key, sensor_id, variable_name_1, variable_1, variable_name_2, variable_2):
    db = get_db()
    cursor = db.cursor()
    apy_key_statement = "SELECT sensor_apy_key FROM Sensor WHERE sensor_id = ?"
    cursor.execute(apy_key_statement, [sensor_id])
    result = cursor.fetchone()
    print(result)
    if result[0] == sensor_apy_key:
        epoch_time = int(time.time())
        statement = "INSERT INTO Sensor_data(sensor_id, variable_name_1, variable_1, variable_name_2, variable_2, time) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(statement, [sensor_id, variable_name_1, variable_1, variable_name_2, variable_2, epoch_time])
        db.commit()
        return True
    else:
        return False
    
def get_sensor_data(company_apy_key, sensor_id, time_from, time_to):
    db = get_db()
    cursor = db.cursor()
    apy_key_statement = "SELECT company_apy_key FROM Sensor,Location,Company WHERE sensor_id = ? AND Sensor.location_id = Location.location_id AND Company.id = Location.company_id"
    cursor.execute(apy_key_statement, [sensor_id])
    result = cursor.fetchone()
    print(result)
    if result[0] == company_apy_key:
        statement = "SELECT * FROM Sensor_data WHERE sensor_id = ? AND time > ? AND time < ?"
        cursor.execute(statement, [sensor_id, time_from, time_to])
        db.commit()
        return cursor.fetchall()
    else:
        return False