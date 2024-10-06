print ("Please enter an amount in cents less than a dollar. ")
cents  = int(input())
Q = cents // 25
cents -= Q * 25
D = cents // 10
cents -= D * 10
N = cents // 5
cents -= N * 5
P = cents
# Q= Quarters, D= Dimes, N= Nickles, P= Pennies/ Cents

print ("Your change will be: ")
print ("Q: ", Q)
print ("D: ", D)
print ("N: ", N)
print ("P: ", P)
