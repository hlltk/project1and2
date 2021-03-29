#********************Project2********************
def rev(x):
    x.reverse() #reverse list "a"
    for i in x:
        if type(i)==list:
            i.reverse() #if type of member of "a" is a list, reverse        
    return x


a=[[1, 2], [3, 4], [5, 6, 7]]
rev(a) #sending a list to rev function
print(a)