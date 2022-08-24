#count the number 4 in a list

#input a list of numbers, seperated by comma
list = list(map(int, input('nhap chuoi:').split(',')))

#code
def count():
    n = 0
    for i in list:
        if i == 4:
            n = n + 1
    
    return n

print('Number of 4 in the list is:', count())