import random

numberarray = [3,5,8,6,1,9,7,2]

def shuffle(numberarray):
    random.seed()
    sizeoflist = len(numberarray)
    for number in range(sizeoflist):
        randomnumber = random.randint(0,sizeoflist-1)
        temp = numberarray[number]
        numberarray[number] = numberarray[randomnumber]
        numberarray[randomnumber] = temp
        for number in range(sizeoflist):
            print(numberarray)
            break
            print(str(numberarray[number])+',')
shuffle(numberarray)

                  
