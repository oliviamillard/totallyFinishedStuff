"""This program will tell the user the top three artists of a given decade or
the top five songs of a given decade. This information is from Billboard
Hot 100 charts."""

#####################
#  Welcome Message  #
#####################

print("Hello and welcome! This program will use information from\nBillboard's Hot 100 Charts to provide answers\nto your questions. Please proceed!")
print("\n")

decade = str(input("What decade are you interested in learning about?\nPlease enter one of the following (w/ apostrophe!) :\n70's, 80's, 90's, 00's, 10's: \n"))
   
print("\n")

achievement = int(input("What achievement are you interested in learning about?\nPlease select one of the following options...\n\nEnter 1 if you want to know the top 3 artists\nof your chosen decade.\n\nEnter 2 if you want to know the top 5 songs\nof your chosen decade.\n\nSo what will it be: "))

print("\n")
if decade == "10's" and achievement == 1:
    print("The top three artists of the 10's are: Rihanna, Katy Perry, and Bruno Mars.")
    print("Rihanna and Katy Perry both have 8 number-one singles.\nBruno Mars has 5.\n")
if decade == "10's" and achievement == 2:
    print('The top 5 songs of the 10\'s are (Title, Artist, # of weeks at #1):\n1. "Blurred Lines", Robin Thicke, 12\n2. "We Found Love", Rihanna, 10\n3. "Happy", Pharrell, 10\n4. "Tik Tok", Ke$ha, 9\n5. "Call Me Maybe", Carly Rae Jepsen, 9\n')

if decade == "00's" and achievement == 1:
    print("The top three artists of the 00's are: Usher, Beyoncé, and Rihanna.")
    print("Usher had 7 number-one singles.\nBeyoncé and Rihanna had 5.\n")
if decade == "00's" and achievement == 2:
    print('The top 5 songs of the 00\'s are (Title, Artist, # of weeks at #1):\n1. "We Belong Together", Mariah Carey, 14\n2. "I Gotta Feeling", The Black Eyed Peas, 14\n3. "Lose Yourself", Eminem, 12\n4. "Yeah!", Usher, 12\n5. "Boom Boom Pow", The Black Eyed Peas, 12\n')

if decade == "90's" and achievement == 1:
    print("The top three artists of the 90's are:\nMariah Carey, Janet Jackson, and Boyz II Men.\nMariah Carey had 14 number-one singles.\nJanet Jackson had 6, Boyz II Men had 5.\n")
if decade == "90's" and achievement == 2:
    print('The top 5 songs of the 90\'s are (Title, Artist, # of weeks at #1):\n1. "One Sweet Day", Mariah Carey and Boyz II Men, 16\n2. "I Will Always Love You", Whitney Houston, 14\n3. "I\'ll Make Love to You", Boyz II Men, 14\n4. "Candle in the Wind", Elton John, 14\n5. "Macarena (Bayside Boys Mix), Los Del Rio, 14\n')

if decade == "80's" and achievement == 1:
    print("The top three artists of the 80's are:\nMichael Jackson, Whitney Houston, and Phil Collins.")
    print("Michael Jackson had 9 number-one singles.\nWhitney Houston and Phil Collins had 7.\n")
if decade == "80's" and achievement == 2:
    print('The top 5 songs of the 80\'s are (Title, Artist, # of weeks at #1):\n1. "Physical", Olivia Newton-John, 10\n2. "Bette Davis Eyes", Kim Carnes, 9\n3. "Endless Love", Diana Ross and Lionel Richie, 9\n4. "Every Breath You Take", The Police, 8\n5. "I Love Rock \'n\' Roll", Joan Jett and the Blackhearts, 7\n')

if decade == "70's" and achievement == 1:
    print("The top three artists of the 70's are:\nBee Gees, Elton John, and Paul McCartney and Wings.")
    print("Bee Gees had 9 number-one singles.\nElton John and Paul McCartney and Wings had 6.\n")
if decade == "70's" and achievement == 2:
    print('The top 5 songs of the 70\'s are (Title, Artist, # of weeks at #1):\n1. "You Light Up My Life", Debby Boone, 10\n2. "Night Fever", Bee Gees, 8\n3. "Tonight\'s the Night (Gonna Be Alright), Rod Stewart, 8\n4. "Shadow Dancing", Andy Gibb, 7\n5. "Bridge over Troubled Water", Simon & Garfunkel, 6\n')

print("\n")
print("Wow! I hope that was fulfilling for you. Thanks for inquiring.")
