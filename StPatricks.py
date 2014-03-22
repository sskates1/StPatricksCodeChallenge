
beer = 99

def displayBeers(beer):
    print (beer,"bottles of beers on the wall!")

def drinkGreenBeer(beer):
    print ("You drank a green beer!")
    beer = beer-1
    displayBeers(beer)
    return beer

def drinkNonGreenBeer():
    print("HEY! We don't serve that kind of beer here.")
    print("We only have green beer")

def restockBeer():
    beer = 99
    print("We got a new shipment!")
    displayBeers(beer)
    return beer

def userInput():
    global beer
    words = input("")
    words = words.strip()
    if words =="drink green beer":
        beer = drinkGreenBeer(beer)
    elif words =="drink beer":
        drinkNonGreenBeer()
    elif words =="restock green beer":
        beer = restockBeer()
    else:
        print("You're at a bar pick something to drink!")

def main():
    global beer
    displayBeers(beer)
    while beer>0:
        userInput()
        if beer <= 10:
            print ("We are low on the green stuff! Time to get more!")
        

        if beer == 0:
            break

if __name__ == "__main__":
    main()
