import Fire
import Water
import Bot

Charmcaster = Water.Water_Wizard(100, 30, 200," ")
Adwatia = Fire.Fire_Wizard(150, 50, 300, " ")
Spellbinder = Water.Water_Wizard(150, 50, 300, " ")
Hex = Fire.Fire_Wizard(125, 30, 250, " ")


p = input("Which magician you want to be? Fire or Water?")
if p == "Water":
    print("Nice, your avatar is Charmcaster")
    Charmcaster.isbot = False
    Spellbinder.isbot = True
    ah = input("Do you want to attack or heal? ")
    if ah == "Heal":
        print(Spellbinder)
        Charmcaster.waterfall(Spellbinder)
        print(Spellbinder)

    elif ah == "Attack":
        a = input("Who do you want to attack, Adwatia or Hex? ")
        if a == "Hex":
            f = input("Should your ally start a battle? ")
            if f == "Yes":
                bot = Bot.bot(Spellbinder, Adwatia)
                print("Adwatia:", Adwatia)
                bot.game()
                print("Adwatia:", Adwatia)
            player = Bot.bot(Charmcaster, Hex)
            print("Hex:", Hex)
            player.game_not_bot()
            print("Hex:",Hex)
        elif a == "Adwatia":
            player = Bot.bot(Charmcaster, Adwatia)
            print("Adwatia: ", Adwatia)
            player.game_not_bot()
            print("Adwatia:", Adwatia)

elif p == "Fire":
    print("Nice you play as Adwatia")
    Adwatia.isbot = False
    Hex.isbot = True

    ap = input("Do you want to attack or heal? ")
    if ap == "Heal":
        print("Hex:", Hex)
        Adwatia.fireball(Hex)
        print("Hex:", Hex)
    elif ap == "Attack":
        h = input("Who do you want to attack, Charmcaster or Spellbinder? ")
        if h == "Charmcaster":
            player = Bot.bot(Adwatia, Charmcaster)
            print("Charmcaster:", Charmcaster)
            player.game_not_bot()
            print("Charmcaster:", Charmcaster)
        elif h == "Spellbinder":
            player = Bot.bot(Adwatia, Spellbinder)
            print("Spellbinder:", Spellbinder)
            player.game_not_bot()
            print("Spellbinder:", Spellbinder)




