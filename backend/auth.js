const bcrypt = require("bcrypt");
const db = require("./db");

const SALT_ROUNDS = 10;

const registerUser = (username, password) => {
    const passwordHash = bcrypt.hashSync(password, SALT_ROUNDS);
    const stmt = db.prepare("INSERT INTO users (username, passwordHash) VALUES (?, ?)");
    stmt.run(username, passwordHash);
};

const authenticateUser = (username, password) => {
    const stmt = db.prepare("SELECT * FROM users WHERE username = ?");
    const user = stmt.get(username);
    if (!user) return false;

    return bcrypt.compareSync(password, user.passwordHash);
};

module.exports = { registerUser, authenticateUser };
