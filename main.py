# Marry-Fuck-Kill in Python
from os import name
import random as rn
import json
from terminaltables import SingleTable


class Player:
    all_player_list = []

    def __init__(self, name) -> None:
        self.name = name
        self.marry = 0
        self.fuck = 0
        self.kill = 0
        Player.all_player_list.append(self)
    def getName(self):
        return self.name
    def raiseMarry(self):
        self.marry += 1
    def raiseFuck(self):
        self.fuck += 1
    def raiseKill(self):
        self.kill += 1
    def getSum(self):
        return self.marry+self.fuck+self.kill
    def getmarrypercent(self):
        if self.getSum() == 0:
            return 0
        else:
            this = 100*self.marry//self.getSum()
            return this
    def getfuckpercent(self):
        if self.getSum() == 0:
            return 0
        else:
            this = 100*self.fuck//self.getSum()
            return this
    def getkillpercent(self):
        if self.getSum() == 0:
            return 0
        else:
            this = 100*self.kill//self.getSum()
            return this
    def getAttribute(self):
        return [self.name, 
        "{} ({}%)".format(self.marry, self.getmarrypercent()),
        "{} ({}%)".format(self.fuck, self.getfuckpercent()),
        "{} ({}%)".format(self.kill, self.getkillpercent())]
    def getAllstats():
        output = [['Charakter', 'Marry', 'Fuck', 'Kill']]
        for character in Player.all_player_list:
            output.append(character.getAttribute())
        return output

class Turn:

    round = 0

    def __init__(self, players, characters) -> None:
        self.players = players
        self.characters = characters
        self.convPlayers()

    def convPlayers(self):
        for i in range(len(self.characters)):
            self.characters[i] = Player(name = self.characters[i])


    def doTurn(self):
        Turn.roundincrement()
        self.format()
        self.request()
        Turn.border()

    def format(self):
        Turn.border()
        print("Runde {runde}".format(runde = Turn.round))
        print("{person}'s Runde".format(person = self.players[Turn.round%len(self.players)]))
        Turn.border()
    
    def space(spaces):
        for _ in range(spaces):
            print(' ')

    def border():
        print('-------------------------')

    def request(self):
        victims = rn.sample(self.characters, k = 3)

        for victim in victims:
            print("Option {i}: {character}".format(i = victims.index(victim)+1, character = victim.name))

        Turn.border()

        correct = False
        while not correct:
            marry = input("Marry: ")
            if Turn.verify(victims, marry):
                obj = Turn.getObject(name = marry, victims= victims)
                victims.remove(obj)
                marry = obj
                correct = True
            else:
                print("Die Eingabe stimmt mit mit keiner der möglichen Antworten überein. Möglich sind: {players}".format(players = [x.name for x in victims]))

        correct = False
        while not correct:
            fuck = input("Fuck: ")
            if Turn.verify(victims, fuck):
                obj = Turn.getObject(name = fuck, victims= victims)
                victims.remove(obj)
                fuck = obj
                correct = True
            else:
                print("Die Eingabe stimmt mit mit keiner der möglichen Antworten überein. Möglich sind: {players}".format(players = [x.name for x in victims]))

        correct = False
        while not correct:
            kill = input("Kill: ")
            if Turn.verify(victims, kill):
                obj = Turn.getObject(name = kill, victims= victims)
                victims.remove(obj)
                kill = obj
                correct = True
            else:
                print("Die Eingabe stimmt mit mit keiner der möglichen Antworten überein. Möglich sind: {players}".format(players = [x.name for x in victims]))
        
        marry.raiseMarry()
        fuck.raiseFuck()
        kill.raiseKill()

    def getObject(name, victims):
        for victim in victims:
            if victim.name == name:
                return victim
        return False

    def verify(players, player):
        for victim in players:
            if victim.name == player:
                return True
        return False
    
    def roundincrement():
        Turn.round += 1



def greetings():
    Turn.border()
    print("""Hey, Herzlich Willkommen beim Spiel Marry-Fuck-Kill\n 
Gib bitte im Folgenden zuerst die Spieler in der Runde an,\n
und danach die Auswahl der Leute, über die sich gestritten werden soll.\n
Falls du mit den Spielern spielen willst, dann gib einfach "SPIELER" ein.\n
Viel Spaß Euch :)
                """)
    Turn.border()
    Turn.space(1)

def playerInput():
    print("Gib im Folgenden bitte einmal alle Spieler an, die mitspielen wollen.")
    players = input("Bitte trenne deine Auswahl mit '-': ")
    Turn.border()
    Turn.space(1)
    return players.split('-')


def characterInput():
    done = False

    while not done:
        print(r"""Gib im Folgenden bitte einmal alle Charaktere an, mit denen ihr spielen wollt.
Ihr habt zum einen die Wahl zwischen verschiedenen Presets, als auch die Option manuelle Inputs zu tätigen,
indem ihr "MANUELL" als Option eingebt.
        """)
        correct = False
        
        while not correct:
            print("Wählt bitte zwischen Folgenden Paketen: ")
            Turn.border()
            with open("presets.json") as f:
                packages = json.load(f)

            for key in packages.keys():
                print(key)
            Turn.border()
            choices = input("Bitte trenne deine Auswahl mit '-': ")
            choices = choices.split('-')

            correct = True
            for choice in choices:
                if not (choice in packages.keys() or choice == "MANUELL"):
                    print("Du hast etwas Falsches eingegeben. Probiere es nocheinmal...")
                    correct = False

        if "MANUELL" in choices:
            print("Gib im Folgenden beiite einmal alle zusätzlichen Charaktere manuell ein.")
            addition = input("Bitte trenne deine Auswahl mit '-':")
        
        characters = []

        for choice in choices:
            if choice != "MANUELL":
                for character in packages[choice]:
                    characters.append(character)
            elif choice == "MANUELL":
                for character in addition:
                    characters.append(character)

        if len(characters) < 3:
            print("Um das Spiel zu spielen, musst du mindestens 3 Charaktere bereitstellen. Versuche es nochmal.")
        else:
            done = True
                
    return characters

def info():
    print("Du kannst das Spiel jederzeit beenden, indem du 'STOP' eingibst.")

def getRounds() -> int:
    print("Wieviele Runden wollt ihr spielen? Keine Eingabe -> 5 Runden")
    done = False
    while not done:
        playerInput = input("Anzahl der Runden: ")
        try:
            playerInput = int(playerInput)
            done = True
        except ValueError:
            print("Bitte eine Zahl eingeben!!")
    
    return playerInput

def main():
    
    rounds_int = 5
    
    greetings()
    players = playerInput()
    rounds_int = getRounds()
    characters = characterInput()
    Turn.border()
    Turn.border()
    Turn.border()
    Turn.space(3)
    Turn.border()

    

    game = Turn(players=players, characters=characters)

    while rounds_int > 0:
        game.doTurn()
        rounds_int -= 1
    
    Turn.border()
    Turn.border()
    Turn.border()
    Turn.space(3)
    Turn.border()

    print("ENDE! Hier sind die Statistiken:")
    table = SingleTable(Player.getAllstats(), title = "Stats")
    print(table.table)



if __name__ == "__main__":
    main()
