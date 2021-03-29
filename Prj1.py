#**********************Project1********************
def flat(x):
    for i in x:
        if type(i)==list:
            flat(i) #if member of "a" is a list it will send the member to flat function
        else:
            new.append(i) #if member of "a" is not list add to "new" list

    return new
   
new=[] #is a empty list
a=[[1,'a',['cat'],2],[[[3]],'dog'],4,5] 
flat(a) #a is a list, sending to flat function
print(new) 




