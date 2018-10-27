import random
import sys

# print histogram values
def printHisto(h, i):
    tot = sum(h)
    for x in h:
        print(i, "\t", x/tot*100)
        i += 1

# Return a number between nbDice and nbDice*6
# following Normal distrib of dice um
def diceProba(nbDice, prob):
    r = random.random()
    i = nbDice
    for x in prob:
        if x > r:
            return i
        i += 1
    print("error")
    return max #this might be an error

# Return a number between nbDice and nbDice*6
# using the sum of nbDice random dice
def diceSum(nbDice):
    r = 0
    for i in range(nbDice):
        r += int(random.random() * 6) + 1
    return r

# Return a number between nbDice and nbDice*6
# following a (dumb) linear distribution
def diceDumb(nbDice):
    return int(random.random() * (6*nbDice-(nbDice-1))) + 1

# Fill 3 histograms with random dice sums
def testDiceProb(nbDice, prob, histoP, histoD, histoS, nbTries):
    for i in range(nbTries):
        a = diceProba(nbDice, prob) - nbDice
        histoP[a] += 1
        a = diceSum(nbDice) - nbDice
        histoD[a] += 1
        a = diceDumb(nbDice) - nbDice
        histoS[a] += 1

# Create proba array and histograms
def init(nbDice):
    diceProba = [
        [1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],
        [1, 3, 6, 10, 15, 21, 25, 27, 27, 25, 21, 15, 10, 6, 3, 1],
        [1, 4, 10, 20, 35, 56, 80, 104, 125, 140, 146, 140, 125, 104, 80, 56, 35, 20, 10, 4, 1]
        ]

    prob = []
    prev = 0.0
    for x in diceProba[nbDice - 1]:
        prob.append(x / (6**nbDice) + prev)
        prev = prob[len(prob) - 1]
    prob[len(prob)-1] = 1.0
    return prob

# Main routine: init dice random system, then call and print the results
def main(nbDice):
    histoProba = [0.0] * (nbDice * 6 - nbDice + 1)
    histoDice = [0.0] * (nbDice * 6 - nbDice + 1)
    histoStupid = [0.0] * (nbDice * 6 - nbDice + 1)
    prob = init(nbDice)

    # Generate
    testDiceProb(nbDice, prob, histoProba, histoDice, histoStupid, 50000)
    print("Probabilist simulation")
    printHisto(histoProba, nbDice)
    print("Sum of random dice")
    printHisto(histoDice, nbDice)
    print("Dumb linear random")
    printHisto(histoStupid, nbDice)

main(int(sys.argv[1]))
