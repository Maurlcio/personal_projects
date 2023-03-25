#!/usr/bin/python3
from random import sample, choice


def name_creator():
    while(1):
        name = input("\nWould you like to generate a full name (type \"generate\" or \"2\")?\
 Or randomize a first name (type \"randomize\" or \"3\")?\nType here: ")

        if name == "randomize" or name == "3":
            consonantsBig = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N",
                             "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
            consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                          "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
            vowels = ["a", "e", "i", "o", "u"]

            print("---------------------")
            print("")
            print("{}{}{}".format(choice(consonantsBig), choice(consonants), choice(vowels)), end="")
            print("{}{}".format(''.join(sample(consonants, 2)), choice(vowels)))
            print("")
            print("---------------------")

        elif name == "generate" or name == "2":
            firstName = ["Airelia", "Seraphine", "Aileen", "Noelle", "Nimiel", "Estelar", "Sheila", "Kolvar", "Baraborn", "Daenys", "Gwen", "Terra", "Eli", "Maya", "Claire", "Aethon", "Myrrh", "Morgan", "Kay", "Cedric", "Irvin", "Glaksha", "Yor", "Gustav", "Lance", "Maria", "Gwendolyn", "Galathea", "Merric", "Jasper", "Cyril", "Grymm", "Leon", "Kaeda", "Kirlia", "Coffer", "Cassemir", "Dana", "Olivia", "Minetta", "Zeke", "Rye", "Wo", "Runo", "Marlina", "Charlotte", "Gia", "Rydia", "Galaka", "Ezir", "Zephyr", "Dianthine", "Saber", "Kana", "Odette", "Merody", "Esmeralda", "Magus", "Ephrais", "Vasylia", "Sol", "Luna", "Stella", "Kali", "Lumity", "Cleo", "Xyn", "Elizabeth", "Pallin", "Melia", "Ghilanna"]
            lastName = ["Atwater", "Agassi", "Apatow", "Akagawa", "Averescu", "Arrington", "Agrippa", "Aiken", "Alexander", "Amado", "Ashsorrow", "Humblecut", "Ashbluff", "Armas", "Akka", "Aoki", "Aldrich", "Apak", "Alinsky", "Desai", "Draper", "Dwyer", "Dixon", "Dalton", "Desmith", "Ditka", "Decker", "Dunlop", "Dumont", "Dandridge", "Diamond", "Dobra", "Dukas", "Agnello", "Alterio", "Bidbury", "Botkin", "Benoit", "Beebe", "Evert", "Elway", "Eslinger", "Ellerbrock", "Eno", "Etter", "Holiday", "Everson", "Ekker", "Kobayashi", "Kicklighter", "Keene", "Kipps", "Willow", "Omen", "Windward", "Grell", "Xanthos", "Quill", "Idlewind", "Rast", "Yarrow", "Yamaguchi", "Winters", "Whesker", "Steele", "Mintz"]

            print("-------------------------------")
            print("")
            if choice(firstName) == "Noelle" and choice(lastName) == "Holiday":
                print("Noelle Holiday")
                print("\nYou're about to meet someone\nvery\nvery\ninteresting")
            else:
                print("{} {}".format(choice(firstName), choice(lastName)))
            print("")
            print("-------------------------------")

        elif name == "quit":
            print("bye bye!")
            return

        else:
            print("nah stop playin")
            return


name_creator()
