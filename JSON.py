from peewee import *

db = SqliteDatabase('my_database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Player(BaseModel):
    Salary = DoubleField()
    Balance = DoubleField()


class Character(BaseModel):
    Name = TextField()
    DOB = DateTimeField()
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
    db = None

    def __init__(self, fileLocation):
        self.fileLocation = fileLocation
        self.db = SqliteDatabase(self.fileLocation)
        try:
            self.connect()
            self.generate_db()
            print(f"Db loaded: {self.fileLocation}")
        except Exception as e:
            print(e)

    def connect(self):
        self.db.connect()

    def generate_db(self):
        db.create_tables([Player, Character, Transaction], safe=True)
