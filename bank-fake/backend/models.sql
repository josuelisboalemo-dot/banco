CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username TEXT,
  password TEXT,
  balance INTEGER
);

CREATE TABLE transactions (
  id INTEGER PRIMARY KEY,
  sender TEXT,
  receiver TEXT,
  value INTEGER,
  date TEXT
);