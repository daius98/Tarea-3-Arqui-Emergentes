CREATE TABLE IF NOT EXISTS Admin(
    username TEXT PRIMARY KEY NOT NULL,
    password TEXT NOT NULL
)
CREATE TABLE IF NOT EXISTS Company(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    company_apy_key TEXT NOT NULL
)
CREATE TABLE IF NOT EXISTS Location(
    location_id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    location_name TEXT NOT NULL,
    location_country TEXT NOT NULL,
    location_city TEXT NOT NULL,
    location_meta TEXT NOT NULL
    FOREIGN KEY (company_id) REFERENCES Company (id)
)
CREATE TABLE IF NOT EXISTS Sensor(
    sensor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id INTEGER,
    sensor_name TEXT NOT NULL,
    sensor_category TEXT NOT NULL,
    sensor_meta TEXT NOT NULL,
    sensor_apy_key TEXT NOT NULL,
    FOREIGN KEY (location_id) REFERENCES Location (location_id)
)
CREATE TABLE IF NOT EXISTS Sensor_data(
    sensor_id INTEGER,
    variable_name_1 TEXT NOT NULL,
    variable_1 FLOAT NOT NULL,
    variable_name_2 TEXT NOT NULL,
    variable_2 FLOAT NOT NULL,
    time INTEGER,
    FOREIGN KEY (sensor_id) REFERENCES Sensor (sensor_id)
)