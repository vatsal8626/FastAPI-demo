from passlib.context import CryptContext
from passlib.hash import bcrypt
# from pwdlib import PasswordHash

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
# pwd_cxt = PasswordHash.recommended()

class Hash():
    #def bcrypt(password: str):
        #return pwd_cxt.hash(password)
    
    def verify(plain_password, hashed_password):
        return pwd_cxt.verify(plain_password,hashed_password)