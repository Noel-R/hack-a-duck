from peewee import *

global db
db = SqliteDatabase("./Game.db")

class BaseModel(Model):
    class Meta:
        database = db


class Player(BaseModel):
    Salary = DoubleField()
    Balance = DoubleField()


class Character(BaseModel):
    Name = TextField()
    Address = TextField()
    Email = TextField()
    CreditScore = IntegerField()
    RiskScore = IntegerField()
    ApprovalState = BooleanField()


class Transaction(BaseModel):
    ID = ForeignKeyField(Character, backref="transactions")
    Merchant = TextField()
    Category = TextField()
    Amount = DoubleField()
    Timestamp = DateTimeField()
    Currency = TextField()
    Status = BooleanField()


class DB:
    fileLocation = ''

    def __init__(self, fileLocation):
        self.fileLocation = fileLocation
        self.db = SqliteDatabase(self.fileLocation)
        try:
            self.connect()
            print(f"Db loaded: {self.fileLocation}")
        except Exception as e:
            print(e)

    def connect(self):
        self.db.connect()
        self.generate_db()

    def generate_db(self):
        db.create_tables(models=[Player, Character, Transaction], safe=True)
