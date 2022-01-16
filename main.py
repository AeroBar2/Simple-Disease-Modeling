#Disclaimer: I am by no means an expert on disease and stuff
#and this disease model is by no means accurate
#ok, disclaimer over

#note: when the disease infects everyone, it just calculates another day
#which isn't supposed to happen.
#Oh well

#additions:
#1. add in a 'recovered' population group

import time
import os

#variables to keep track of populations
reproductive_number = 1.2 #the "R" number of the disease
suspectable = 1000 #the number of people who can catch the disease
infected = 0 #the number of infected people
total_population = suspectable + infected

#clears the screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


#the function that 'models' the disease
def main(suspectable, infected, total_population):
    cls()
    print("Disease spread model")
    set_r_number = float(input("Enter a reproductive number from 0.1 to 10 (1.2 by default): "))
    reproductive_number = set_r_number
    if reproductive_number > 10:
        reproductive_number = 10
    elif reproductive_number < 0.1:
        reproductive_number = 0.1
    print("Beginning...")
    infected += 1
    suspectable -= 1
    time.sleep(1.5)
    fully_infected = False
    day = 1
    while not fully_infected:
        if infected > 1000:
            infected = 1000
            suspectable = 0
            fully_infected = True
            print(f"The disease has fully infected the population in around {day} days.")
            break
        else:
            print(f"Day {day}")
            infected *= reproductive_number
            suspectable = total_population - infected
            print(f"Infected: {round(infected)} ({round(infected / 1000 * 100)}%)")
            print(f"Susceptible: {round(suspectable)} ({round(suspectable / 1000 * 100)}%)")
            print("Total Population: 1000 \n")
            day += 1
            time.sleep(1)


main(suspectable, infected, total_population)