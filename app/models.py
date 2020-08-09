from app import db
from werkzeug.security import check_password_hash, generate_password_hash
import datetime



class User(db.Document):
    username = db.StringField()
    password = db.StringField()
    email = db.EmailField()
    point = db.IntField(default=0)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

    def clean(self):
        self.password = generate_password_hash(self.password)
        super(User,self).clean()
        

    def check_password(self,password):
        return check_password_hash(self.password,password)

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

class Player(db.EmbeddedDocument):
    title = db.StringField(default="Rasim")
    age = db.IntField(default=15)


class GameRoom(db.Document):
    members = db.ListField(db.EmbeddedDocumentField(Player),default=list)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
