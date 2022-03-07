#imports all of the necessary modules for this project
from datetime import datetime
import random, time
#sets the current time as a variable for the timer
ct = datetime.now()
now,now2=ct.strftime("%M%S"),ct.strftime("%M%S")
#sets all necessary global variable
random_choice,user_answer,total_time=None,'',''
score,score2,timer,out_of_time,run_1_time=0,0,100,0,0
scoresheet='D:/Yr11/DIT/Python/Quiz assessment/scoresheet_holder/scoresheet.txt'
yes=['y','Y','yes','Yes','YES','yEs','yES','yep','ok','yeah','Yeah','YEAH','Ye','ye','YE']

#a list containing all of the questions to pull out later
questions=['How many teeth does an adult human have?\na.30\nb.32\nc.34\nd.36\n',
'What is the largest bird of prey in the world?\na.Andean Condor\nb.Bald Eagle\nc.Peregrine Falcon\nd.Common Buzzard\n',
'In which sport would you use a shuttlecock?\na.Volleyball\nb.Extreame Frisbe\nc.Badminton\nd.Rugby League\n',
'Who is fifth in line to the British throne?\na.Prince Andrew\nb.Prince Harry\nc.Meghan Markle\nd.Prince Louis\n',
'What is the biggest state in America?\na.Califronia\nb.Texas\nc.Alaska\nd.New York\n',
'Who wrote Snow White And The Seven Dwarves?\na.The Brother Grimm\nb.Disney\nc.Roald Dahl\nd.Judy Blume\n',
'What is the capital of Hawaii?\na.Honolulu\nb.Hilo\nc.Kapolei\ndLihue\n',
'Enchiladas originated in which country?\na.Spain\nb.Italy\nc.Brazil\nd.Mexico\n',
"In Dirty Dancing, what is Baby's first name?\na.Paul\nb.Frances\nc.Jeffery\nd.Francios\n",
'How many eggs does the average chicken lay per year?\na.21\nb.300\nc.70\nd.260\n',
'In which English seaside town was ‘Fawlty Towers’ set?\na.Brighton\nb.Whitby\nc.Torquay\nd.Hastings\n',
'What is a group of lions called?\na.Pride\nb.Pack\nc.Scool\nd.Hazard\n',
'Where would you find the River Thames?\na.Egypt\nb.Venis\nc.London\nd.Auckland\n',
'What animal alive today is even bigger than a dinosaur?\na.Elephant\nb.Kamodo Dragon\nc.Blue Whale\nd.Sperm Whale\n',
'What alcohol do you traditionally use to flame a Christmas pudding?\na.Brandy\nb.Vodka\nc.Whiskey\nd.Mead\n',
'What is a baby kangaroo called?\na.Joey\nb.Pup\nc.Hopper\nd.Kid\n',
'What is the name of the fictional town where the series Stranger Things is set?\na.Spring Field, California\nb.Halkins, Indiana\nc.Twin Peaks, Washinton\nd.Mayberry, North Carolina\n',
'What year did Rihanna achieve global success with the mega-hit "Umbrella"?\na.2005\nb.2010\nc.2012\nd.2007\n',
'Name the slowest animal in the world.\na.Garden Snail\nb.Three toed sloth\nc.Two toed Sloth\nd.African Giant Brown Snail\n',
'Is the sun a star or a planet?\na.A Star\nb.A Planet\n',
'What are the names of Harry Potter’s parents?\na.John and ELinor\nb.Paul and Bonnie\nc.James and Lily\nd.Samuel and Pheobe\n',
'What is the capital city of Spain?\na.Barcelona\nb.Madrid\nc.Valencia\nd.Seville\n',
'Who plays Tommy Shelby in Peaky Blinders?\na.Cillian Murphy\nb.Finn Cole\nc.Paul Anderson\nd.Tom Hardy\n',
'How many legs does a lobster have?\na.6\nb.12\nc.8\nd.24\n',
'How many Michelin stars does Restaurant Gordon Ramsay in London currently hold?\na.1\nb.2\nc.3\nd.4\n',
"What's the best selling book of all time?\na.Harry Potter\nb.The Hungry Caterpillar\nc.Catcher in the Rye\nd.The Bible\n",
'Botany is the study of what?\na.Atoms\nb.Animals\nc.Robots\nd.Plants\n',
'To the tip - how tall is the Eiffel Tower?\na.245m\nb.324m\nc.598m\nd.185m\n',
'Sofia is the capital of which country?\na.Bulgaria\nb.Serbia\nc.Isreal\nd.Fiji\n',
"What is the name of James Corden's character in Gavin & Stacey?\na.Jackie\nb.Johny\nc.Fluffy\nd.Smithy\n",
'Who famously said "You must be the change you wish to see in the world."\na.Helen Keller\nb.Steven Halking\nc.Mahatma Gandhi\nd.George Bush\n',
'Which is the only venomous snake native to the UK?\na.Grass Snake\nb.Dotted Python\nc.Adder\nd.King Snake\n',
"Arctic Monkeys took the indie scene by storm in 2005 with the now classic 'I Bet You Look Good on the Dancefloor' - but what's the first line of the song?\na.'Stop making the eyes at me I'll stop making the eyes at you'\nb.'Have you got colour in your cheeks?'\nc.'The mirror's image, it tells me it's home time'\nd.'Well, I wrote my number down.'\n",
'What planet is known as the red planet?\na.Mars\nb.Venus\nc.Saturn\nd.Deta-C42\n',
'What is the name of the Greek dip consisting of yoghurt and cucumber?\na.Hummus\nb.Tzatziki\nc.Greek Feta Dip\nd.Athens Ohm\n',
'Catalonia is a region of what country?\na.Italy\nb.Greece\nc.Spain\nd.Portugal\n',
'Who wrote Oliver Twist?\na.Roald Dahl\nb.Beatrix Potter\nc.Rick Riordan\nd.Charles Dickens\n',
"What colour is a giraffe's tongue?\na.Pink\nb.Blue\nc.Purple\nd.Green\n",
'What do you call a group of jellyfish?\na.A Bloom\nb.A Scool\nc.A Tingle\nd.A Cloud\n'
]

#a dictionary with all the quetsions and corresponding answers
answer_to_questions={
  questions[0] : 'b',
  questions[1] : 'a',
  questions[2] : 'c',
  questions[3] : 'd',
  questions[4] : 'c',
  questions[5] : 'a',
  questions[6] : 'a',
  questions[7] : 'd',
  questions[8] : 'b',
  questions[9] : 'd',
  questions[10] : 'c',
  questions[11] : 'a',
  questions[12] : 'c',
  questions[13] : 'c',
  questions[14] : 'a',
  questions[15] : 'a',
  questions[16] : 'b',
  questions[17] : 'd',
  questions[18] : 'b',
  questions[19] : 'a',
  questions[20] : 'c',
  questions[21] : 'b',
  questions[22] : 'a',
  questions[23] : 'c',
  questions[24] : 'c',
  questions[25] : 'd',
  questions[26] : 'd',
  questions[27] : 'b',
  questions[28] : 'a',
  questions[29] : 'd',
  questions[30] : 'c',
  questions[31] : 'c',
  questions[32] : 'a',
  questions[33] : 'a',
  questions[34] : 'b',
  questions[35] : 'c',
  questions[36] : 'd',
  questions[37] : 'b',
  questions[38] : 'a'
}

#the main menu which displays scores and other similar things at the end of the quiz then saves answer to a sheet in case the user wants to view previous scores
def menu(score_placeholder1,score_placeholder2):
  global yes, scoresheet
  print(f"You had one minute to complete as many questions as possible. \n\nIn that time you got a score of {score_placeholder1}")#displays the scores
  view_scores=str(input("Do you want to view your previous scores?[Y, N]\n"))
  try:
    #opens file off of my USB and reads the file then it prints it out on the screen if the user typed in yes
    if view_scores in yes:
      scoresheet_file=open(scoresheet, 'r')
      print(scoresheet_file.read())
      scoresheet_file.close()
    save_score=str(input("Do you want to save your score? [Y, N]\n"))
    #asks the player if they want to then save their score to the score sheet and if so it appends it onto the end of the file
    if save_score in yes:
      scoresheet_file=open(scoresheet, 'a')#opens the file
      scoresheet_file.write(str(score_placeholder1))#wriets the new score onto the file
      scoresheet_file.write('\n')
      scoresheet_file.close()#closes the file again
    reset_scoresheet=str(input("If you want to reset the scoresheet type out 'RESET' (cap sensitive)\n"))#ask user if they want to reset the scoresheet
    #if they want to reset the scoresheet it deletes everything on the sheet then resets the title back in
    if reset_scoresheet=='RESET':#they have to type in RESET all caps so that way they can't accidently reset it if they accidently typed in yes for example
      scoresheet_file=open(scoresheet, 'w')
      scoresheet_file.write('List of previous scores:\n')
      scoresheet_file.close()
  except FileNotFoundError:#tries to save the answer to the score text file although if the USB isn't plugged in it won't be able to save the scores so instead it plays this code
    print("\n\n\033[1;31mPlease enter USB and go onto an offline python interpreter to view scoresheet\033[0;37m\n")#changes the text colour to red and displays warning
  play_again=str(input("do you want to play again? [Y, N]\n"))#sees if the user wants to play the quiz again if so it plays the game function again else it exits
  if play_again in yes:
    print('ok, have fun :)')
    game()
  else:
    exit('ok then, goodbye :)\n\n(the code ending now is purposeful dispite what repl says :) it isnt a glitch)\n')#exits the code if the user input that thye dont want to play again

#this is a simple function that resets the current time for the timer
def reset_timer():
    global user_answer, random_choice, now, now2, timer, score, score2#gets all the useful global variables
    if int(now)>int(now2)+timer:#checks if time is up or if there is still time left
        menu(score,score2)#if there is no time left it skips it and goes to the menu
    else:#else it resets the current time
        ct = datetime.now()
        now=ct.strftime("%M%S")

#function that takes the set time to count to and the current time then displays it in a readable fasion
def time_left(time_placeholder,time2_placeholder):
    global total_time,timer,run_1_time#gets the useful variables
    total_time=''#resets the total time variable to nothing every time the time left function is used
    time_left_unreadable=int(time2_placeholder)+timer-int(time_placeholder)#works out the amount of time left although it is not readable
    time_left_unreadable= str(time_left_unreadable)#it turns the variable from an int to an str for the for loop
    for readable_time in time_left_unreadable:#for loop that turns the non user friendly time into a user friendly displayed time by inserting a semi-colon in the right spot
        total_time=total_time+readable_time
        if len(total_time)==1:#checks how many digits inside the number left to put the semi-colon in the correct place and make it readable
            total_time=total_time+':'
    if len(total_time)==3:#checks how many digits inside the number left to put the semi-colon in the correct place and make it readable
        total_time=total_time.replace(":",'')
        total_time=int(total_time)
        if total_time >60:
            total_time=total_time-40
        total_time=str(total_time)
        total_time="0:"+total_time#adds a 0 at the start to represent the minutes then a semi-colon if there is only seconds left
    elif len(total_time)==2: #checks how many digits inside the number left to put the semi-colon in the correct place and make it readable
        total_time=total_time.replace(":",'')
        total_time="0:0"+total_time
    return total_time

#this askes the player a question and saves the answer as a variable
def question():
  global user_answer, random_choice, now, now2, timer, out_of_time#gets necessary variables
  reset_timer()#resets the current time
  print(f"you have {time_left(now,now2)} left")#uses time left circuit to show the player how much time they have left
  random_choice=random.choice(questions)#picks a random question from the list
  user_answer=str(input(random_choice))#asks the question to the player
  questions.remove(random_choice)#removes the question from the list so that way you don't get repeats of questions

#this funtion takes the players answer then checks if it is the correct answer
def validater():
  global user_answer, random_choice, score, timer, now, now2, out_of_time #gets all useful global variables
  reset_timer()#uses the reset timer function to update the current time
  user_answer=user_answer.lower()#sets the user answer to lowercase that way if they had caps lock on but got the correct answer it would be marked correct
  answer=answer_to_questions.get(random_choice)#gets the corresponding answer to asked question
  if answer==user_answer:#checks if the user answer and real answer if so adds 1 to the score
    print("correct\n\n")
    time.sleep(0.3)
    score+=1
  elif user_answer !='a' and user_answer !='b' and user_answer !='c' and user_answer !='d':#if it isn't correct it checks if the answer is within the boundary case of a b c d if wrong they it tells the user what they should answer plus get 5 seconds minused from their timer
    print("\n\033[1;31mPlease enter 'a','b','c' or 'd' next time\nAs punishment you get minus 5 seconds from your time\033[0;37m\n\n")#changes colour to red to give a warning to use the inputs within the boundary case
    time.sleep(0.3)
    if timer==100 or timer>100:#removes 5 seconds from the timer as a punishment
      timer-=40
    timer-=5
  else: #otherwise it is an incorrect answer in which case they get 5 seconds minused from their timer
    print("incorrect\nYou get a punishment of minus 5 seconds\n\n")
    time.sleep(0.3)
    if timer==100 or timer>100:#checks if the timer is in minutes or seconds as yuo need to minus 40 from the minute (1:00) to get the seconds (60)
        timer-=40
    timer-=5

def game():#main game function so that way you can loop it later to replay
  global user_answer, random_choice, score, timer, now, now2, out_of_time,total_time,run_1_time
  #resets main variables as when you replay it starts from scratch
  ct = datetime.now()
  now,now2=ct.strftime("%M%S"),ct.strftime("%M%S")
  random_choice,user_answer,total_time=None,'',''
  score,score2,timer,out_of_time,run_1_time=0,0,100,0,0
  #this is the timer circuit that will continue asking the player questions and checking the answers until 1 minute has passed
  while int(now)<int(now2)+timer:
    ct = datetime.now()#reset the current time so to update timer
    now=ct.strftime("%M%S")
    if questions == []:#checks if the question list as although it is highly unlikely to impossible for it too be empty it checks for jsut in case to save the code from breaking
      print("you ran out of questions :0\n")
      break
    question()#goes to the circuit that picks out question and asks it
    validater()#checks if the given answer is correct
  menu(score,score2)#once the timer is up it goes to the menu page where it displays the scores
print("Welcome to a timed quiz you have one minute to complete as many questions as possible. you will get one point for evry question you get correct but you will get 5 seconds minused for every question you get wrong.")
time.sleep(1)
game() #starts the code
