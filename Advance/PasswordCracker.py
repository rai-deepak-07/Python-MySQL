#Program to simulate a brute-force password cracker

import string, os, time
from random import randint

# Step 01: Take password from user
pswd = input("🔐 Enter the password: ")

# Step 02: Define all possible characters
keys = []
keys.extend(list(string.digits)) 
keys.extend(list(string.ascii_letters))
keys.extend(list(string.punctuation)) 
keys.extend(list(string.whitespace)) 

# Step 03: Initialize variables
pwg = ""
attempts = 0
start_time = time.time()

print("\n🚀 Starting password attack...")
time.sleep(1)

# Step 04: Keep guessing until password matches
while pwg != pswd:
    pwg = ""
    attempts += 1
    
    # Step 05: Generate random password of same length
    for i in range(len(pswd)):
        guessPass = keys[randint(0, len(keys) - 1)]
        pwg = str(guessPass) + str(pwg)
        
        print(f"🧠 Guessing: {pwg}")
        print("⚡ Attacking... please wait!")
        time.sleep(0.05)   # realism delay
        
        os.system("cls" if os.name == "nt" else "clear")

# Step 06: Calculate total time
end_time = time.time()
total_time = end_time - start_time

# Step 07: Show final result
print("✅ PASSWORD CRACKED!")
print("🔓 ------------------------")
print(f"🔑 Password   : {pwg}")
print(f"🔁 Attempts   : {attempts}")
print(f"⏱️ Time Taken : {total_time:.2f} seconds")
print("🎉 Crack Successful!")
