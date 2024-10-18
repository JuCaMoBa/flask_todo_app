from repositories.user_respository import UserRepository

from werkzeug.security import generate_password_hash, check_password_hash

class AuthService():

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, name, email, password):
        hash_password= generate_password_hash(password, method='pbkdf2:sha256')
        self.user_repo.insert_user(name, email, hash_password)
        
    def check_credentials(self, credentials):
        user = self.user_repo.select_user(credentials)
        if not user or not check_password_hash(user['password'], credentials['password']):
            return None
        return user
    
    def check_email(self, credentials):
        user = self.user_repo.select_user(credentials)
        return user
           
       
  


        

    


        



