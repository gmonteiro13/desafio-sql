CREATE TABLE clients (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE sellers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    region TEXT,
    team TEXT
);

CREATE TABLE sales (
    contract_id TEXT PRIMARY KEY,
    client_id INTEGER,
    seller_id INTEGER,
    type TEXT,
    date DATE,
    category TEXT,
    duration INTEGER,
    value REAL,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (seller_id) REFERENCES sellers(id)
);