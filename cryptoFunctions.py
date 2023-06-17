from passlib.hash import argon2
import secrets

def hash_password(password, salt):
    hash = argon2.using(rounds=16, memory_cost=47104, parallelism=4, salt=salt).hash(password)
    return hash

def create_salt():
    return secrets.token_bytes(64)