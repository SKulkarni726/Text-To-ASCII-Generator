beginning = True

#Defining the different characters


#Numbers:

one = '''

    11111
   1    1
        1
        1
        1
        1
    1111111 '''
    
two = '''
   22222
  2     2
       2
      2
     2
   2
  22222222 '''

three = '''
 33333
 33   3
      33
  33333
      3
3     3
 33333 '''

four = '''
      4
     4 4
    4  4
   4   4
  4    4
  444444
       4
       4
       4
       4 '''

five = '''
5555555
5
5
 55
    5
      5
      5
     5
55555 '''

six = '''
666666
6     6
6
6666666
6      6
6      6
66666666 '''

seven = '''
7777777
     7
    7
   7
  7
 7
7 '''

eight = '''
 888
8   8
 888
8   8
 888 '''

nine = '''
 9999
9    9
9    9
 99999
     9
  99
99   '''

zero = '''
  000
 0   0
 0   0
 0   0
 0   0
  000  '''
#Symbols:

bulldog = '''

,-.___,-.
\_/_ _\_/
  )O_O(
 { (_) }
  `-^-'  '''

exclamationmark = '''
       !!!
       !!!
       !!!
       !!!
       !!!
       !!!
       !!!

       !!!
      !   !
       !!!  '''
questionmark = '''
 ???????????
??        ??
?        ??
        ??
       ??
      ??
      ??
      ??
      ??

       ?
     ?  ?
       ?  '''
unknown = '''
________________
|              |
|              |
|              |
|              |
|      ?       |
|              |
|              |
|              |
|______________|  '''
#If  there is a symbol that isn't in the program, rather than completly ending the loop, it replaces it with a symbol saying it is unknown

period = '''
  ....
 ......
........
 ......
  .... '''

comma = '''
    ,,,
   ,,,,
  ,,,,,
,,,,,  '''

appostrophe = '''
  ||||||||
   ||||||
    ||||
     ||  '''
# I can't make an appostrophe out of appostrophes since it will end the string


#Letters:
      
A = '''
     AAA
    A   A                          
   A     A                                
   A      A                            
  AAAAAAAAAA                           
 A          A                                
A            A '''

Z = '''

  ZZZZZZZZ
        Z
       Z
      Z
     Z
    Z
  ZZZZZZZZ '''

Y = '''
  Y     Y
   Y   Y
    Y Y
     Y
     Y
     Y
     Y  '''

X = '''
 X        X
  X      X
    X   X
      X
    X   X
  X       X
 X         X '''
 
W = '''
W       W        W
 W     W W      W
  W  W   W     W
   W W     W  W
    W        W      '''
V = '''
  V           V
   V         V
    V       V
     V     V
      V   V
       V V
        V     '''

U = '''
   U        U
   U        U
   U        U
   U        U
    UU    UU
      UUUU '''
T = '''
    TTTTTTT
       T
       T
       T
       T
       T
       T'''
S = '''
     SSSSS
    S
    S
    SSSS
        S
  S     S
   SSSSSS'''
R = '''
    RRRRRR
    R    R
    R    R
    RRRRR
    R    R
    R     R
    R      R '''

Q = '''
     QQQQQ
    Q     Q
    Q  Q  Q
    Q   Q Q
    QQQQQQQ
          Q
           Q '''

P = '''
    PPPPPP
    P    P
    P    P
    PPPPP
    P
    P
    P    '''

O = '''
     OOOOO
    O     O
    O     O
    O     O
     OOOOO '''

N = '''
    NN   N
    N N  N
    N  N N
    N   NN
    N    N'''

M = '''
    M           M
    MM         MM
    M  M      M M
    M   M M M   M
    M     M     M
    M           M  '''

L = '''
     L
     L
     L
     L
     L
     LLLLLLLL'''

K = '''
     K      K
     K     K
     K    K
     KKKKK
     K    K
     K      K '''

J = '''
    JJJJJJJJJJ
        JJ
          J
           JJ
    JJ      JJ
      JJ     JJ
       JJJJJJJJ  '''

I = '''
    IIIIIII
       I
       I
       I
       I
       I
    IIIIIII'''

H = '''
    H    H
    H    H
    H    H
    HHHHHH
    H    H
    H    H
    H    H'''

B = '''
    BBBBBB
    B    B
    B    B
    BBBBB
    B    B
    BBBBBB'''
    
C = '''
     CCCCC
    C
    C
    C
    C
     CCCCC'''

D = '''
    DDDD
    D   D
    D   D
    D   D
    D   D
    DDDD '''

E = '''
    EEEEEE
    E
    EEEEEE
    E
    EEEEEE'''

F = '''
    FFFFFF
    F
    F
    FFFFF
    F
    F '''
G = '''
    GGGGG
   GG
   G
   G    
   G  GGGGG
   G      G
    GGGGGG '''





while beginning:
    #A While loop, which allows the program to run how every many times the user wants
    
    print('''  Vertical Text To ASCII Generator
  _________________________________

            Please enter your text:
            ''')

    message = input()
    uppermessage = message.upper()
#Asking for input and turning it into a list in order to separate the individual letters
    message_list = list(uppermessage)

    finalmessage = " "
    newline = '''

    '''
    number = 0
    #Creating empty variables to store the information of the function, and a number that will keep going up as you go from one letter to the next
    start = True
 
    def choosing_letter ():
        global number
        global finalmessage
        global newline
        global start
        while start:
        #A loop that is continously checking for every letter, and if it doesnt find it, it checks for the next

            if number >= len(message_list):
                start = False
                return finalmessage
        #Looking to see if the list has ended, in which cases the function is ended and the finalmessage is returned

        #Everything under this is continous guessing and checking for certain characters
        #Whenever it finds a character that is in that certain number position in the string it adds that ascii art to the string which may or may not already contain part of the string
        #It the increases the number by one, indicating that it has found the character and will move on to the next (if there is another character)
        #The newline makes it so the message is more readable and less clumped together

        #Symbols:
        
            elif message_list[number] == " ":
                finalmessage += 3 * newline
                number = number + 1
            elif message_list[number] == ".":
                finalmessage += period
                finalmessage += newline
                number = number + 1
            elif message_list[number] == ",":
                finalmessage += comma
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "'":
                finalmessage += appostrophe
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "?":
                finalmessage += questionmark
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "!":
                finalmessage += exclamationmark
                finalmessage += newline
                number = number + 1

        #Letters:
            elif message_list[number] == "A":
                finalmessage += A
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "B":
                finalmessage += B
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "C":
                finalmessage += C
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "D":
                finalmessage += D
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "E":
                finalmessage += E
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "F":
                finalmessage += F
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "G":
                finalmessage += G
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "H":
                finalmessage += H
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "I":
                finalmessage += I
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "J":
                finalmessage += J
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "K":
                finalmessage += K
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "L":
                finalmessage += L
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "M":
                finalmessage += M
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "N":
                finalmessage += N
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "O":
                finalmessage += O
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "P":
                finalmessage += P
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "Q":
                finalmessage += Q
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "R":
                finalmessage += R
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "S":
                finalmessage += S
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "T":
                finalmessage += T
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "U":
                finalmessage += U
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "V":
                finalmessage += V
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "W":
                finalmessage += W
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "X":
                finalmessage += X
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "Y":
                finalmessage += Y
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "Z":
                finalmessage += Z
                finalmessage += newline
                number = number + 1

        #Numbers:

            elif message_list[number] == "1":
                finalmessage += one
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "2":
                finalmessage += two
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "3":
                finalmessage += three
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "4":
                finalmessage += four
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "5":
                finalmessage += five
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "6":
                finalmessage += six
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "7":
                finalmessage += seven
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "8":
                finalmessage += eight
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "9":
                finalmessage += nine
                finalmessage += newline
                number = number + 1
            elif message_list[number] == "0":
                finalmessage += zero
                finalmessage += newline
                number = number + 1


            


            
            else:
                finalmessage += unknown
                finalmessage += newline
                number = number + 1
                #If it isn't listed it is seen as an unknown character
    #checking to see if the message is related to Bulldogs, which in this case means it will display a picture of a bulldog.
    if  message == "Bulldog":
        print(bulldog)
    elif message == "Bulldogs":
        print(bulldog)
    elif message == "bulldog":
        print(bulldog)
    elif message == "bulldogs":
        print(bulldog)
    else:
        choosing_letter()
        print(finalmessage)
    #Asking if the user wants to continue, which is why the whole program is in a while loop.
    answer = input(''' Would you like to continue?
    Yes or No?

    ''')
    if answer == "Yes":
        beginning = True
        #Continuing the program
        print(" ")
    elif answer == "No":
        beginning = False
        #Stopping the Program
        print(" ")
        print("Thank you!")
        
    else:
        print("Please answer exactly either 'Yes' or 'No'")
        #Making sure to get an exact answer
        print(" ")
        response = input()
        if response == "No":
            beginning = False
            print(" ")
            print("Thank you for using!")
        elif response == "Yes":
            beginning = True
        else:
            #If the response is anything besides "Yes" or "No" then the program just stops automatically.
            beginning = False
            print(" ")
            print("Thank you for using!")

            
        

