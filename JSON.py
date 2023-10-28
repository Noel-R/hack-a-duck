import jsonpickle


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
    Balance = 0
    Salary = 0

    def __init__(self, playerData):
        print(playerData)
        self.Salary = playerData.Salary
        self.Balance = playerData.Balance

    def generate(self):
        self.Balance = 100
        self.Salary = 100


class Game:
    firstLoad = False
    days = []

    def __init__(self, gameData):

        self.firstLoad = gameData.Game.firstLoad

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
        self.Game = data['Game']
        self.Player = data['Player']
        self.Characters = data['Characters']

    def getJSON(self):
        return {
            "Player": self.Player,
            "Characters": self.Characters,
            "Game": self.Game
        }


class DataFile:
    fileLocation = ''
    readData = ''
    gameData = {}

    def __init__(self, location):
        self.fileLocation = location
        self.read()

    def read(self):
        with open(self.fileLocation, "r") as file:
            self.readData = jsonpickle.decode(file.read())
            self.gameData = GameData(self.readData)

    def write(self):
        with open(self.fileLocation, "w") as file:
            file.write(jsonpickle.encode(self.gameData.getJSON()))
        print("Game saved.")


def main():
    file = DataFile("./data.json")


main()
