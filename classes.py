import random
import math

CLASSES = {
    7: [ 'Helen', 'Shakil', 'Eric', 'Jennifer Y', 'Jennifer Z', 'Arif', 'Queenie', 'Jawadul', 'Shaina', 'Vivien', 'Brian', 'Naotaka', 'Bayan', 'Adam', 'Caleb', 'Terry', 'Jason', 'Alessandro', 'Samantha', 'Carol', 'Joyce', 'Shannon', 'Charles', 'Taylor', 'Kelly', 'Leo', 'Khyber', 'Ibnul', 'Eugene', 'Yuyang', 'Karina', 'Tiffany', 'Holden', 'Michael'],
    8: ['Masha', 'Adrian', 'David', 'Eric', 'Josh', 'Jerome', 'Henry', 'Jackie', 'Giorgio', 'Karen', 'Sonal', 'Xavier', 'Bermet', 'Alex', 'Iris', 'Manahal', 'Donia', 'Md', 'Connie', 'Lisa', 'Xing', 'Angelica', 'Angel', 'Augie', 'Dimitriy', 'Yiduo', 'Gordon', 'Tiffany', 'Clive', 'Jonathan', 'Sasha', 'Daniel'],
    9: [ 'Yu Qi', 'Michela', 'Kristin', 'Fabiha', 'Maxim', 'Marcus', 'Ish', 'James', 'Ryan', 'Edward', 'Adeeb', 'Jake', 'Cynthia', 'Kevin', 'Levi', 'Edmond', 'Kyle', 'Andrew', 'Max', 'Jenny', 'Philip', 'Shan', 'Mansour', 'Ray', 'Jake', 'Ida', 'Kerry', 'Stanley', 'Jackie', 'William', 'Tina', 'Michael']
}

# This is the method created for the assignment
def randomStudent(number):
    li = CLASSES[number]
    random_int =  random.randint(0, len(li) - 1)
   #Test case: print random_int
    return li[random_int]


# This method randomly selects from all 3 classes and returns the number of times it takes to find Mansour's name. Just for fun to see how much random.randint() hates him :)
def howmanytimes():
    i = 0
    count = 0
    while i == 0:
        if randomStudent(random.randint(7,9)) == 'Mansour':
            i+=1
            return count
        else:
            count+=1

# ...And this counts how many times it takes for the program to get Mansour's name on the first try :P
'''j = 0
count2 = 0
while j == 0:
    if howmanytimes() == 1:
        j+=1
        print count2
    else:
        count2+=1
    
'''

#Test cases for assignment method
print randomStudent(7)
print randomStudent(8)
print randomStudent(9)
