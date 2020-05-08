from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key= True)
	username = db.Column(db.String(64), index = True)
	email = db.Column(db.String(120), index = True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<User {}>'.format(self.username)