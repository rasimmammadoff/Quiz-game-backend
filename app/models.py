from app import db
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
import random, string



class User(db.Document):
    username = db.StringField()
    password = db.StringField()
    email = db.EmailField()
    point = db.IntField(default=0)
    win = db.IntField(default=0)
    lose = db.IntField(default=0)
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
    name = db.StringField()
    word = db.StringField(default="")
    found_letters = db.ListField(db.StringField(),default=list)

    

class GameRoom(db.Document):
    members = db.ListField(db.EmbeddedDocumentField(Player),default=list)
    waiting = db.BooleanField(default=True)
    currentQuestion = db.StringField(default="")
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)


class Word(db.Document):
    word = db.StringField(max_length=7)
    usage = db.IntField(default=0)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)


class Question(db.Document):
    question = db.StringField()
    answer = db.ListField()
    correct_index = db.IntField(default=0)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

class PlayerAnswer(db.EmbeddedDocument):
    username = db.StringField()
    answer = db.StringField()


class AnsweredQuestion(db.Document):
    answers = db.ListField(db.EmbeddedDocumentField(PlayerAnswer))
    bothAnswered = db.BooleanField(default=False)
    room = db.ReferenceField(GameRoom)
    question = db.ReferenceField(Question)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)



