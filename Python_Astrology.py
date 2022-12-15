import random
name = input("please enter your name so I may give you your REAL Astrology fortune: ").capitalize()
nameList = []
nameList.append(name)
firstLetter = nameList[0][0]

#this is a list of verbs to use
verbs = ["criticize","tear","pin","cope","constitute","summon","calculate","tax","extend","change","situate","consult","arrest","laugh","enquire","reproduce","remark","lock","open","shrug","speed","ride","characterize","suspect","design","force","see","evaluate","precede","register","update","restrict","forget","land","head","shut","miss","weigh","swim","frown","breathe","arrive","wander","ease","protest","charge","crawl","emphasize","care","state"]
#this is a list of nouns
nouns = [
'people','history','way','art','world','information','map','two','family','government','health','system','computer','meat','year','thanks','music','person','reading','method','data','food','understanding','theory','law','bird','literature','problem','software','control','knowledge','power','ability','economics','love','internet','television','science','library','nature','fact','product','idea','temperature','investment','area','society','activity','story','industry','media','thing','oven','community','definition','safety','quality','development','language','management','player','variety','video','week','security','country','exam','movie','organization','equipment','physics','analysis','policy','series','thought','basis','boyfriend','direction','strategy','technology','army','camera','freedom','paper','environment','child','instance','month','truth','marketing']
#this is a list of adverbs
adverbs = []
#this is a list of adjectives
adjective = []
#this will return a random verb from the list of verbs
def randomVerb():
    return verbs[random.randint(0,len(verbs))]
print("RANDOM VERB TEST: "+ randomVerb())
#this will return a random noun from the list of nouns
def randomNoun():
    return nouns[random.randint(0,len(nouns))]
print("random test popopy scoopity: "+ randomNoun())


match name:
    case "Drew":
        print("If you want to "+randomVerb()+" your profession to the next level, you'll need to "+randomVerb()+" some adjustments Possably by "+randomVerb()+" a deer. Identify the goals you wish to achieve such as assasinating JFK. "+randomVerb().capitalize()+" the pillars of your actual literal house that support your house may be necessary if you wish to "+randomVerb()+" not having your house collaps(rlly tho get that shit checked out), "+randomVerb()+" a new level of fire, or "+randomVerb()+" a different direction in your career. "+randomVerb().capitalize()+" yourself with the right people.")

    case "Andrew":
        print("Today is the day to show your worth, as you will undoubtedly face some difficult conditions in the office. As a result, maintaining your mental clarity will be crucial. Joining a team of passionate people is an opportunity to put your people skills and ability to persuade to good use. The vibrant environment will encourage you to work together to conquer any challenges.")

    case "Kenny":
        print(" There could be new ways to advance financially and professionally. It might be something you gave up on that turns out to be practical in the end, like a concept, or it could be a person who introduces you to new professional opportunities, or it could be an object that turns out to be useful. It's going to be fun to branch out and try new things right now. Take advantage of the situation.")
    
    case "Sasha":
        print("Situations at work are going to heat up. Expect the unexpected, since everything looks unpredictable. Your usual schedule, habits, and routines may be abruptly altered at the last minute. The future may seem very different from what you are doing now. The place or job you have is also subject to change. Hold off on your expectations until things are settled.")

    case "David":
        print("YOu  WILL D I E AAAAAAAA THIS IS A BAD FORTUNE BUT ALSO You are probably feeling aggravated at work today. You may feel like you're not getting anything done because of things that are beyond your influence. You are being evaluated based on your achievement, but you don't feel like you're getting fair credit. Talk to your manager about it today; there's no need to wait. They are more likely to respond to what you have to say.")
    case _:
        print("Welp I guess your name isnt in the Ancient scrolls so your just gona idk explode tomorrow SO SAITH THE ACNANT SOCIETY WHICH AMRKS WHAT PEOPLE DO ALL DAY")
match firstLetter:
    case "A":
        print("poop")
    case "B":
        print('damn')
    case "C":
        print("poop")
    case "D":
        print('damn')
    case "E":
        print("poop")
    case "F":
        print('damn')
    case "G":
        print("poop")
    case "H":
        print('damn')
    case "I":
        print("poop")
    case "J":
        print('damn')
    case "K":
        print("poop")
    case "L":
        print('damn')
    case "M":
        print("poop")
    case "N":
        print('damn')
    case "O":
        print("poop")
    case "P":
        print('damn')
    case "Q":
        print("poop")
    case "R":
        print('damn')
    case "S":
        print("poop")
    case "T":
        print('damn')
    case "U":
        print("poop")
    case "V":
        print('damn')
    case "W":
        print("poop")
    case "X":
        print('damn')
    case "Y":
        print("poop")
    case "Z":
        print('damn')
    case _:
        print("you don't have a name so your like super cursed man")


