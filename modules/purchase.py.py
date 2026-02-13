CREATE TABLE IF NOT EXISTS purchase_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset_id TEXT,
    requested_by TEXT,
    description TEXT,
    status TEXT
);
