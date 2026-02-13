CREATE TABLE IF NOT EXISTS assets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset_id TEXT,
    asset_name TEXT,
    department TEXT,
    location TEXT,
    capacity TEXT,
    make TEXT,
    model TEXT,
    amc_expiry DATE,
    criticality TEXT
);
