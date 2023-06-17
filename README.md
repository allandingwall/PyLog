# PyLog
PyLog is a secure and user-friendly Python-based implementation of a login system. It uses SQLite as its database management system and implements the Argon2id algorithm for secure password hashing.



## Installation & Usage Guide
### Initialising the database

To initialise the database, use the following command: 

`sqlite3 database.db < init.sql`


### Usage

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mattis, neque in faucibus vehicula, nibh velit pretium urna, in sodales sem nisl quis nunc. Integer egestas ultricies turpis commodo porttitor. Phasellus eu posuere elit. Maecenas placerat metus lectus, nec mollis libero suscipit vel. Fusce cursus neque ac egestas accumsan. Maecenas vitae accumsan libero. Proin vel ullamcorper massa, vel malesuada nibh. Praesent tempor tellus id massa aliquet ullamcorper. Ut est nibh, cursus eget viverra at, sollicitudin non orci. 

## Specifications
### Password Hashing
Passwords are hashed using the Argon2id hashing algorithm with a configuration of 16 rounds, 47104 kibibyte memory usage, and 4 threads of parallelism, meeting and exceeding the [minimum recommendations made by OWASP for password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#argon2id).

## Future Changes / To-Do
- [ ] Finish how-to guide
- [ ] Integrate change password function
- [ ] Add pepper to database
- [ ] Integrate Flask to deploy a web application for login portal
- [ ] Implement 2-factor authentication
