from werkzeug.security import generate_password_hash, check_password_hash
passw = generate_password_hash("abc123!!",method="pbkdf2:sha256")
print(passw)
print(check_password_hash(passw,"abc123!!"))