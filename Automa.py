import random
new_input = input("The Length Of The Board Should Be: ")
new_input2 = input("The Height Of The Board Should Be: ")
try:
    test = int(new_input)
    test2 = int(new_input2)
except:
    print("Error")
    quit()
generation = 1
def randomizer():
    random_number = 2 - random.randint(1, 2)
    if random_number == 0:
        return "⬜"
    else:
        return "⬛"
newsquare = ""
def square_add():
    global newsquare
    x = 1
    while x <= int(new_input):
        newsquare += randomizer()
        x += 1
y = 1
while y <= int(new_input2):
    square_add()
    if y < int(new_input2):
        newsquare += "\n"
    y += 1
print(newsquare + "\nGeneration " + str(generation))
counter = 0
def self_replicate():
    global counter
    global newsquare
    global generation
    newnewsquare = ""
    for s in newsquare:
        try:
            test = newsquare[counter + 1]
            if "⬜" in s and "⬛" in newsquare[counter + 1]:
                newnewsquare += randomizer()
            elif "⬛" in s and "⬜" in newsquare[counter + 1]:
                newnewsquare += "⬜"
            else:
                newnewsquare += s
        except:
            newnewsquare += s
        counter += 1
    new_input = input("Continue (C) Or Terminate (Any Other Key)? ")
    new_input = new_input.lower()
    if new_input == "c":
        generation += 1
        counter = 0
        newsquare = newnewsquare
        print(newnewsquare + "\nGeneration " + str(generation))
        newnewsquare = ""
        self_replicate()
    else:
        quit()
self_replicate()

