import pandas as pd
import string
from random import SystemRandom
import numpy as np
import os.path

np.random.seed(1)

offers_from = ['Brand', 'Product recommendation']
associate_values =["Jeans","Lowers","Shrugs","Watches","Books"]

def Choose_associationtype():
    secure_proc = SystemRandom()
    return secure_proc.choice(offers_from)

def Choose_associationvalue():
    secure_proc = SystemRandom()
    return secure_proc.choice(associate_values)


#   print("\nThe choice from list={} is as follows:\n{}".format(offers_from, secure_proc.choice(offers_from)))

# def randomString(stringLength=10):
#     """Generate a random string of fixed length """
#     offers_from = ['Google', 'Microsoft', 'Amazon', 'Apple', 'IBM', 'Oracle']
#     return ''.join(random.choice(ChooseAnOffer()) for i in range(stringLength))

# def random_associationvalue(stringLength=10):
#     """Generate a random string of fixed length """
#     letters = "aabb"
#     return ''.join(random.choice(ChooseAnOffer()) for i in range(stringLength))
print(offers_from)
lst = []
for i in range(5000000):
    lst.append(Choose_associationtype())


newlst = []
for i in range(5000000):
    newlst.append(Choose_associationvalue())


data2 = pd.DataFrame(
    {"userid": np.arange(1, 5000001), "associationtype": lst, "associationvalue":newlst})
#          {"userid": np.arange(1, 100),  "associationrank": np.random.randint(low=0, high=100, size=99)})
path = os.getcwd()
data2.to_csv(path + "/randata.csv",index=False)
print(data2)
