numbers = [12, 45, 7, 89, 23, 56,89]
largest=0
seclargest=0

for i in numbers:
    if i > largest:
         seclargest=largest
         largest=i
        
    elif i<largest and i>seclargest:
        seclargest=i    
print(largest)
print(seclargest)

# move all zeroes to the end

numbers = [0, 5, 0, 3, 8, 0, 2]
nonzero=[]

for j in numbers:
    if j!=0:
     nonzero.append(j)

nonzero.append(0)
nonzero.append(0)
nonzero.append(0)

print(nonzero)

