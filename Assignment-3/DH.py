import random
import hashlib

# read in prime
with open('prime', 'r') as f:
    p = int(f.read())

# set generator
g = 2

# create a random 64 bit number for salt
salt = random.getrandbits(64)

# username and password
username = "alice"
password = "password123"

# create the private key
private_key = hashlib.sha256(f"{username}:{password}:{salt}")

# create the public key
public_key = pow(g, private_key, p)

# output key to file as hex
with open('public_key', 'w') as f:
    f.write(hex(public_key))

# get other person's public key later
other_public_key = 0

# create the shared key
shared_key = pow(other_public_key, private_key, p)

# hash the shared key and output
shared_key = hashlib.sha256(shared_key)