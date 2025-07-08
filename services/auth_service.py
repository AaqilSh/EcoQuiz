import os	
from werkzeug.security import generate_password_hash, check_password_hash

class AuthService:
	def __init__(self, users_file="users.json"):
		self.admin_username = os.getenv('ADMIN_USERNAME', 'admin')
		self.admin_password_hash = os.getenv('ADMIN_PASSWORD_HASH', 
                                           generate_password_hash('admin'))

	def verify_admin_credentials(self, username, password):
		if username == self.admin_username:
			return check_password_hash(self.admin_password_hash, password)
		return False
	