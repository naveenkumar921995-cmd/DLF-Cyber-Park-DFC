CREATE TABLE IF NOT EXISTS energy_readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meter_name TEXT,
    date TEXT,
    reading REAL
);
