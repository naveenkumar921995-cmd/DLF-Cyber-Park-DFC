CREATE TABLE IF NOT EXISTS work_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    shift TEXT,
    asset_id TEXT,
    department TEXT,
    work_type TEXT,
    priority TEXT,
    description TEXT,
    downtime REAL,
    spares TEXT,
    status TEXT,
    created_by TEXT
);
