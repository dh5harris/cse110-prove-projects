#intro
print('\nWelcome to your adventure!\n')
print('Your choices are in ALL CAPS, but you can always enter a choice of your own if you want.\n')
#To personalize some messages
name = input('What is your name? ')

#This if statement asks to begin the game or not
begin = input(f'{name.capitalize().strip()} would you like to begin? YES or NO: ')
if begin.lower().strip() == 'yes':
    #This if statement begins the first level, three choices, one is hidden, and an else
    path = input('You are lost walking down a forest path at night. You come to a fork in the path. Do you take the RIGHT path or the LEFT path? ')
    if path.lower().strip() == 'right':
        #This if statement begins the second level, two choices and an else
        hungry = input('Your stomach starts growling. Do you EAT the rest of your trailmix or do you DRINK some water? ')
        if hungry.lower().strip() == 'drink':
            print('The water was refreshing.')
            #This if statement begins the third level, three choices and an else
            sound_one = input('You hear a sound in the bushes behind you. Do you turn around and LOOK, do you go and INVESTIGATE what the sound is, or do you RUN the other way? ')
            if sound_one.lower().strip() == 'run':
                print('You end up running into a stream. Fresh water! Cool!')
                print('You see someone approaching you. They ask you a question.')
                #This if statement is a fun Monty Python Holy Grail question
                answer = input('"I need to know how to find out if a witch is a witch or not. Real witches are made of wood. What can I use to weight the witch to see if she will float or not and know if she is made of wood?" ')
                if answer.lower().strip() in('a duck', 'duck'):
                    print('You are wise beyond your years and must be a King')
                else:
                    print('Are you a peasant? I do not think that will help.')
            elif sound_one.lower().strip() == 'look':
                print('It turns out that you see just a rabbit, but that is no ordinary rabbit. It has nasty, big, pointy teeth. It is the most foul, cruel, and bad tempered rodent, that has a vicious streak a mile wide. It is a killer. Seeing you do not have a holy hand granade, you wisely and slowly back away from it to live a another day.')
            elif sound_one.lower().strip() == 'investigate':
                print('You see a swollow trying to carry a coconut. You wonder how can a five ounce bird can carry a one pound coconut and maintain its air-speed velocity.')
            else:
                print(f'{name.capitalize()}, that does not make any sense. Please restart your adventure.')
        elif hungry.lower().strip() == 'eat':
            print('The trail mix is delicious')
            feel = input('You feel something rub against your leg. It is a skunk. Do you STAY STILL or FREAK OUT? ')
            if feel.lower().strip() == 'freak out':
                print('Your night just got worse. You were sprayed by the skunk.')
            elif feel.lower().strip() == 'stay still':
                print('Your patience pays off and the shunk walks off. You don not get sprayed')
            else:
                print('That was not a choice. You still get sprayed by the skunk. Try the adventure again.')
        else:
            print(f'{name.capitalize()}, that is not a chioce. Please try your adventure again.')
    elif path.lower().strip() == 'left':
        flashlight = input('The batteries in the flashlight you have been using die. Do you KEEP GOING or CAMP out for the night? ')
        if flashlight.lower().strip() == 'camp':
            print('You find a spot that looks comfy.')
            camp = input('While you are getting your camp ready, you notice bright lights coming down the path. Do HIDE or ASK for directions? ')
            if camp.lower().strip() == 'ask':
                print('The person is lost too. You now have a new hiking buddy!')
            elif camp.lower().strip() == 'hide':
                print('The person sees you anyways. Turns out that they are lost too. You have a new hiking buddy!')
            else:
                print(f'{name.capitalize()}, that is not a choice. Please try again.')
        elif flashlight.lower().strip() == 'keep going':
            print('You keep going. The moonlight is bright enough.')
            sound_two = input('You hear a sound behind you. Do you keep WALKING or do you TURN AROUND? ')
            if sound_two.lower().strip() == 'turn around':
                print('It is the rest of your hiking group. They have been looking for you. You have been saved!')
            elif sound_two.lower().strip() == 'walking':
                print('You keep walking. It turns out that the sound was from a bear, a hungry bear. He gobbles you up in one bite. You die.')
            else:
                print(f'{name.capitalize()}, what are you trying to do? That did not work. Try again. ')
        else:
            print(f'{name.capitalize()}, you have to chose one or the other. {flashlight.capitalize()} is not a choice. Try again.')
    #First level hidden choice
    elif path.lower().strip() == 'turn around':
        print('You retraced your steps to find yourself back out of the forest and no longer lost. You go home safely.')
    else:
        print(f'{path.capitalize()} is not a choice. Please try again.')
else:
    print(f'Wait, what? Really? You chose {begin.lower()}? That was completely unexpected and a little awkward. Well, Try again...please.')
