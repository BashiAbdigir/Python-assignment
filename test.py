"""""
print("Welcome to the Mad Lib Generator!")
print("Let’s create a wild story. Just answer a few quick questions...")

name = input("Enter a name: ")
adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
ingword = input("Enter a verb ending in -ing: ")
place = input("Enter a place: ")
number = int(input("Enter a number: "))


print("Great! Here’s your story:")

story = "Once upon a time, everyone in "  + place + "were " + ingword + "in joy as they lived in harmony until a " + adj + name + "attacked. Their "+ str(number) + " years of peace has came to an end all because of the destructive weapon: " + noun

print(story)
"""""

"""""

billAmount = int(input("Enter the bill amount: "))
tipPerc = int(input("Enter the tip percentage: "))
taxPerc = int(input("Enter the tax percentage: "))
split = int(input("The bill is split across how much people?: "))

taxNbill = taxPerc / 100 * billAmount
tipNbill = tipPerc / 100 * billAmount

print("Subtotal:  $" + str(billAmount) )
print("Tax (" + str(taxPerc) + "%): " + str(taxNbill))
print("Tip (" + str(tipPerc) + "%): "+ str(tipNbill))

print("Subtotal:  $" + str(billAmount + taxPerc + tipNbill) )
print("Each person owes:  $" + str((billAmount + taxPerc + tipNbill) / split) )
"""""

"""""
mbti = ''

print("Question 1")
print("Which one are you?")
print("A. Extrovert")
print("B. Introvert")


choice = input("You choice: ")

if choice.lower() == 'a':
    mbti += "E"
else:
   mbti += "I"

print("Question 2")
print("Which one are you?")
print("A. Sensors")
print("B. Intuitives")

choice = input("You choice: ")

if choice.lower() == 'a':
     mbti += "S"
else:
    mbti += "N"
    

print("Question 3")
print("Which one are you?")
print("A. Thinker")
print("B. Feeler")

choice = input("You choice: ")

if choice.lower() == 'B':
    mbti += "T"
else:
    mbti += "F"
    
print("Question 4")
print("Which one are you?")
print("A. Judger")
print("B. Perceiver")

choice = input("You choice: ")

if choice.lower() == 'B':
    mbti += "J"
else:
    mbti += "P"
    
    
print("calculating results...")
print("Your MBTI is :" + mbti)
print("Research it to learn more about yourself!! :)")
"""""

"""""
total = 0
highest = 0
lowest = 100
for i in range(3):
    grade = float(input("Enter a grade:"))
    total += grade
    if grade >= highest:
        highest = grade
    elif grade <= lowest:
       lowest = grade 

total = total / 3

print("Your average: " + str(round(total, 1)))

if total >= 90:
    print("Excellent work!")
elif total > 80:
    print("Great job")
elif total > 70:
    print("Youre doing well, keep it up")
elif total > 60:
    print("You're passing, but there's room to grow.")
elif total < 60:
    print("Lets make a plan to improve")
else:
    print("Error!!")
    
print("Your highest mark was: " + str(float(highest)))
print("Your lowest mark was: " + str(float(lowest)))
"""""
"""""
import random

randomNum = random.randint(1, 100) 
print(randomNum)

print("Pick a name number between 1-100")
choice = int(input("Choice: "))
tries = 0

while randomNum != choice:
    tries += 1
    if choice == randomNum:
        break
    elif choice < randomNum:
        print("Too Low!!")
        if randomNum - 10 < choice:
            print("Getting hot!!")
        choice = int(input("Choice: "))
    elif choice > randomNum:
        print("Too High!!")
        if randomNum + 10 > choice:
            print("Getting hot!!")
        choice = int(input("Choice: "))
    else:
        print("Error!!")
    
print("Got the number in " + str(tries) + " tries!!")

"""""


def count_vowels(word):
    vowels = 0
    for letter in word:
        if letter.lower() == 'a' or letter.lower() =='e' or letter.lower() =='i' or letter.lower() =='o' or letter.lower() == 'u':
            vowels += 1 
    return vowels
    
def first_and_last(word):
    newStr = ''
    if len(word) != 1:
           newStr = word[0]  + word[-1]
    else:
           newStr = word[0]  + word[0]
    return newStr
    
    
def contains_target(word, target):
    for letter in word:
        if target in word:
            return 'Found [' +  target + '] in [' + word + ']'
        else:
            return "Didn't Find [" +  target + "] in [" + word + "]"
    
    
def reverse_case(word):
    return word.swapcase()

def find_letter_position(word, letter):
    position = word.find(letter)
    print("Looking for the letter '" + letter + "' position : " + str(position))
   

def print_intro():
    print("Welcome")
    wordOrPhrase = input("Enter a word: ")
    wordOrPhrase = wordOrPhrase.strip().lower() 
    trg = input("What letter do you wanna look in your word?: ")
    ltr = input("What letter's position do you wanna look in your word?: ")
    print("Vowel count: " + str(count_vowels(wordOrPhrase)))
    print("First and last letters: " + first_and_last(wordOrPhrase))
    print("Looking for the letter '" + trg + "' : " + (contains_target(wordOrPhrase, trg)))
    find_letter_position(wordOrPhrase, ltr)
    print("Reversed capitalizaition: " + reverse_case(wordOrPhrase))
    
print_intro()


