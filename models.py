from main import db

class User(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	Username1=db.Column(db.String(20))
	Username2=db.Column(db.String(20))

	def __repr__(self):
		return f"User('{self.Username1}','{self.Username2}')"
