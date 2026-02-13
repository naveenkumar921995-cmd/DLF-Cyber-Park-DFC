CREATE TABLE IF NOT EXISTS compliance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    compliance_type TEXT,
    department TEXT,
    issue_date TEXT,
    expiry_date TEXT,
    status TEXT
);
