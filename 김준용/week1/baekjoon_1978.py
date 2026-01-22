count = int(input())
values = set(map(int, input().split()))
how_many_prime=0
prime_set=[2]

#prime number generation
for i in range(1, max(values)+1):
    nope=False
    for prime in prime_set:
        if ((i==1) or (i%prime==0)): #is it 1 or can it be divided by a value in the prime list? Then get out
            nope=True
            break
    if nope:
        continue
    else:
        prime_set.append(i) #Adds new prime number to list

for value in values: #compares prime list and given list
    if (value in prime_set):
        how_many_prime+=1
print(how_many_prime)
