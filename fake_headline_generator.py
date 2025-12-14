#start the program
#import the random module
import random

#create subjects
subjects =["shahrukh khan",
           "virat kohli",
           "nirmala sitaraman",
           "a mumbai cat",
           "A group of monkey",
           "prime minister modi",
           "auto rikshaw driver from delhi"]


actions =["launches",
          "cancels",
          "dances swith",
          "eats",
          "declares war on",
          "orders",
          "celebrates"]


places_or_things =["at red fort",
                   "in Mumbai local train",
                   "a plate of samosa",
                   "Inside Parliament",
                   "at Ganga ghat",
                   "during Ipl match",
                   "at India gate"]

#start the headline generator loop
while True:
    subjects = random.choice(subjects)
    actions = random.choice(actions)
    places_or_things = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subjects} {actions} {places_or_things} "
    print("\n" + headline)

    user_input =input("\n do you want another headline? (yes/no)").strip().lower()
    if user_input =="no":
        break

    #print goodbye message
    print("\n Thanks for using the fake headlne generator.have a fun day")