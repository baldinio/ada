# a= 2;
# print(type(a));
# a= "mama";
# print(type(a));
# a= True;
# print(type(a));
#
# # THIS IS A COMMEMT
#
# a= "mami" + " loves me "+ \
#     'very much'
# #we can't use comments after using \
# # \ is the line continuation character
# print(a)
#
# a='Don\'t go there!'
# print(a)
#
# b="Don't go there!"
# print(a)
#
# c=''' "Don't go there!", mama said.'''
# print(c)
#
# d="""Don't go there! mama said."""
# print(d)

def demoFuntion(x):         #defining a function
    print(x,"id1=",id(x))
    x=42
    print(x,"id2=",id(x))

x=4
demoFuntion(x)
print(x,"id_main=",id(x))

list1=[1,2,3.14,"mama","tata",[5,6],True];
print(list1)
print(list1[5][0])

print("\n","demoFunction2")
def demoFunction2(*p2):
    print(p2,"id = ",id(p2))
    #p2=[10,11,12]
    p2+=(10,11,12)
    print(p2,"id = ",id(p2))

demoFunction2(*list1)
print(list1,"id = ",id(list1))

for i in range(len(list1)):
     print(list1[i])

print("\n")

for i in range(2,len(list1)):
    print(list1[i])

print("\n")

for i in range((len(list1)-1),-1,-1):
    print(list1[i])