# PyLog
PyLog is a Python-based login portal designed to provide robust security through the usage of SQLite and Argon2. This project aims to demonstrate the implementation of a secure authentication system that ensures the safe storage of user passwords.

### Password Hashing Function
Passwords are hashed using the Argon2id hashing algorithm for secure storage of passwords, with a configuration of 16 rounds, 47104 kibibyte memory usage, and 4 threads for parallelism, exceeding the [minimum recommendations made by OWASP for password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#argon2id).

## Future Changes
- Integrate Flask to deploy a web application for login portal.
- Change password function.
