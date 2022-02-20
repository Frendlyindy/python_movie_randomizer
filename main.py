import random 
movie_list = []
user_input = 0
num_choice = -1

class User:
  def __init__(guy, _name):
    guy.name = _name
  
  

def readFile(fileName):
         #opens the file in read mode
        words = file.read().splitlines() #puts the file into an array
        return words
u1 = User('Bradley')
print('Welcome ' +u1.name+ '! Please choose what you would like to do [enter num]: ')
while num_choice != '0':
    
    print('1 - Add Movie to File')
    print('2 - Randomize Movie to watch')
    print('3 - See all Movies in File')
    print('0 - Quit Program')
    num_choice = input('- ')
    if num_choice == '1':
        file = open("movies.txt", "a")
        user_input = input('Enter the movie you wish to add: ')
        file.write(user_input + '\n')
        file.close()
    elif num_choice == '2':
      file = open('movies.txt', "r")
      movie_list = readFile(file)
      print('You should watch - ' + random.choice(movie_list))
      file.close()

    elif num_choice == '3':
        file = open('movies.txt', 'r')
        print(file.read())
        file.close()



