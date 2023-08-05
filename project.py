import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
'New York': 'Albany', 'North Carolina': 'Raleigh', 
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiznum in range(35):
    quizfile = open(f'D:\\Automation Python\\FileHandling\\QuizFiles\\Quiz{quiznum+1}.txt', 'w')
    answerfile = open(f'D:\\Automation Python\\FileHandling\\QuizFiles\\Answer{quiznum+1}.txt', 'w')

    quizfile.write('Name: ' + '\n' + 'Roll Number: \n\n')
    quizfile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quiznum+1))
    quizfile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionnum in range(50):
        correct = capitals.get(states[questionnum])
        wronganswers = list(capitals.values())
        del wronganswers[questionnum]
        wronganswers = random.sample(wronganswers, 3)
        answeroptions = wronganswers + [correct]
        random.shuffle(answeroptions)

        quizfile.write(f"\n{questionnum+1}. What is the capital of {states[questionnum]} state? \n")
        for i in range(4):
            quizfile.write(f"   {'ABCD'[i]}. {answeroptions[i]}\n")
        quizfile.write('\n')

        answerfile.write(f"\n{questionnum+1:02d}: {'ABCD'[answeroptions.index(correct)]}")
    
    quizfile.close()
    answerfile.close()


