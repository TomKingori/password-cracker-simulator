# Password Cracker Simulation

## Overview
This project is a **password brute-force simulation** that demonstrates how attackers attempt to crack credentials. It includes:
- A **Node.js web app** with user authentication.
- A **Python brute-force script** for testing login security.
- Support for **username-password combinations** and **hash cracking**.
- Multi-threading for faster attacks.

## Installation
### 1️. Clone the Repository
```sh
git clone <REPO_URL>
```

### 2️. Setup the Backend (Node.js)
```sh
cd backend
npm install
npm run dev
```
➡ **Backend runs on `http://localhost:3000`**

### 3️. Setup the Brute-Force Script (Python)
```sh
pip install -r requirements.txt
```

## Running the Attacks
### **1️. Brute-Force Attack with Usernames & Passwords**
```sh
python brute_force.py -u usernames.txt -p passwords.txt
```

### **2️. Brute-Force Attack with Credentials File (username:password)**
```sh
python brute_force.py -c creds.txt
```

### **3️. Hash-Based Attack**
```sh
python brute_force.py -hf hashes.txt -ht sha256 -w wordlist.txt
```