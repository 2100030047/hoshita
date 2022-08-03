import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist=["jadega","ashwin","rahane","shami","dhoni","virat"]
mylist1=["jadega","ashwin","rahane","shami","dhoni","virat"]
print(random.choice(mylist))
#print(random.choice(mylist))
random.shuffle(mylist)