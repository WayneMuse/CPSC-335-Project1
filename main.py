from alg1 import find_starting
from alg2 import min_swaps

def main():
    cont = True
    while cont:
        print("Choose which algorithm question")
        algchoice = input("Type 1 for Algorithm 1: Greedy Approach to Hamiltonian Problem\n" "Type 2 for Algorithm 2: Connecting Pairs of Persons\n" "Type 3 to Exit\n")
        if algchoice == '1':
            print("======================================")
            print("Greedy Approach to Hamiltonian Problem\n")
            citydistances = list(map(int, input("City Distances: ").split()))
            Fuel = list(map(int, input("Fuel: ").split()))
            print(Fuel[0], type(Fuel[0]))
            Mpg = int(input("Mpg: "))
            print("Starting City is", find_starting(city_distances=citydistances,fuel=Fuel,mpg=Mpg))   
            print()
        elif algchoice == '2':
            print("======================================")
            print("     Connecting Pairs of Persons      \n")
            input_row = list(map(int, input("Input: ").split()))
            print("Output: ",min_swaps(input_row))
            print()
        elif algchoice == '3':
            print("======================================")
            print("               Exiting        ")
            cont = False
        else:
            print("\n+++++++++++[Invalid input, try again]++++++++++++\n")

if __name__ == "__main__":
    main()
    
###main
    ##while continue loop
    ##prompt user input
        ##if input 1 run algor 1
            #get input for city_distances
            #get input for fuel
            #get input for mpg 
            #run alg1 with inputs
        ##if input 2 run algor 2
            #get input for rows
            #run alg2 with input
        ##if input 3 exit
            #exit
        ##else try again