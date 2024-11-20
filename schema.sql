CREATE TABLE clients (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE sellers (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE teams (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE seller_teams (
    seller_id INTEGER,
    team_id INTEGER,
    PRIMARY KEY (seller_id, team_id),
    FOREIGN KEY (seller_id) REFERENCES sellers(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE sales (
    contract_id TEXT PRIMARY KEY,
    client_id INTEGER,
    seller_id INTEGER,
    type TEXT,
    sale_date DATE,
    category TEXT,
    region TEXT,
    contract_duration INTEGER, -- in months
    value REAL,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (seller_id) REFERENCES sellers(id)
);