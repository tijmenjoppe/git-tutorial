LANG = "EN"


def check_antwoord(antwoord):
    return antwoord == 42


def hello_world(lang):
    if lang == "NL":
        return "Hallo wereld!"
    elif lang == "FR":
        return "Bonjour le monde!"
    else:
        return "Hello world!"


def main():
    print(hello_world(LANG))

    antwoord = input("Wat is het antwoord op de ultieme vraag van het leven, het universum, en alles?")
    if check_antwoord(antwoord):
        print("Correct!")
    else:
        print("Mogelijk heb je een andere vraag in je hoofd?")

# Tijmen's functionaliteit wordt hier toegevoegd:
# TODO:
# * meer talen

# test()
main()
