const Database = require("better-sqlite3");

const db = new Database("users.db");
db.exec(`
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        passwordHash TEXT
    )
`);

module.exports = db;