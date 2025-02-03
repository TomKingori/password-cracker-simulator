const express = require("express");
const cors = require("cors");
const path = require("path");
const { registerUser, authenticateUser } = require("./auth");

const app = express();
app.use(express.json());
app.use(cors());
app.use(express.static(path.join(__dirname, "../frontend")));

// Register Route
app.post("/register", (req, res) => {
    const { username, password } = req.body;
    try {
        registerUser(username, password);
        res.json({ message: "User registered successfully" });
    } catch (err) {
        res.status(400).json({ error: "Username already exists" });
    }
});

// Login Route
app.post("/login", (req, res) => {
    const { username, password } = req.body;
    if (authenticateUser(username, password)) {
        res.json({ message: "Login successful" });
    } else {
        res.status(401).json({ error: "Invalid credentials" });
    }
});

// Start Server
const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
