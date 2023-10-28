import json


class Day:
    dayNumber = 0
    dayName = ''
    checkedCharacters = []

    def __init__(self, num, checkedChars):
        self.dayNumber = num
        self.checkedCharacters = checkedChars

        match self.dayNumber:
            case 0:
                self.dayName = "Monday"
            case 0:
                self.dayName = "Tuesday"
            case 0:
                self.dayName = "Wednesday"
            case 0:
                self.dayName = "Thurday"
            case 0:
                self.dayName = "Friday"


class Character:
    name = ''
    dob = ''
    address = ''
    email = ''
    creditScore = ''
    riskScore = ''
    approved = False

    def __init__(self, characterData):
        pass


class Player:
    balance = 0
    salary = 0

    def __init__(self, playerData):
        if playerData['balance'] is None or playerData['salary'] is None:
            self.generate()

    def generate(self):
        self.balance = 100
        self.salary = 100


class Game:
    firstLoad = False
    days = []

    def __init__(self, gameData):
        if gameData['firstLoad']:
            self.firstLoad = True

        if self.firstLoad:
            self.generate()

    def generate(self):
        for i in range(0, 5):
            self.days.append(Day(i, []))
        self.firstLoad = False


class GameData:
    Player = {}
    Game = {}
    Characters = []

    def __init__(self, data):
        self.parseData(data)

    def parseData(self, data):

        if data['game'] is None or data['player'] is None or data['characters'] is None:
            self.Game = Game({'firstLoad': True})
            self.Player = Player({})
            self.Characters = []
            return

        self.Game = Game(data['game'])
        self.Player = Player(data['player'])
        for char, _ in data['characters']:
            self.Characters.append(Character(char))


class DataFile:
    fileLocation = ''
    readData = ''
    gameData = {}

    def __init__(self, location):
        self.fileLocation = location
        self.read()

    def read(self):
        with open(self.fileLocation, "r") as file:
            self.readData = json.load(file)
            self.gameData = GameData(self.readData)

    def write(self):
        with open(self.fileLocation, "w") as file:
            json.dump(self.gameData, file)
        print("Game saved.")


def main():
    file = DataFile("./data.json")
    file.write()


main()
