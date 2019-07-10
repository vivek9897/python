# print("hello")

####################
# var = 20
# print(var,end="-")
# print("var")
# var1 = input("enter a name")
# var =  int(input("enter a name"))
# print(var1)
# print(var)


########taking input
# name = input("enter an name")
# city = input("enter city name")
# num = int(input("enter phone no"))
# print("name is  ",name,"city is",city,"number  is",num)

#############learning licence
# age = int(input("enter your age"))
# if(age>18):
#     print("ok")
# elif(age>=16 and age<18):
#     print("learning licence")
# else:
#     print("not eligible")

######loops
# for i in range(10,0,-2):
#     print("hello",i)
# for i in range(0,11):
#     print(i*4)

########function
# def funk():
#     for i in range(0,4):
#         print("hello",i)
#     print("outside")
# funk()
# def funk(a,b):
#     sum = a+b
#     print(sum)
#     print("outside")
# funk(2,3)



# a = int(input("enter a digit"))
# b = int(input("enter a digit"))
# c = a+b
# print(c)
# a = int(input("enter a digit"))
# b = int(input("enter a digit"))
# c= int(input("enter a choice \n1.addition\n2.subtraction\n3.division\n4.multiplication\n"))
# if(c==1):
#     d=a+b
#     print(d)
# elif(c==2):
#     d=a-b
#     print(d)
# elif(c==3):
#     d=a/b
#     print(d)
# elif(c==4):
#    d=a*b
#    print(d)
# else:
#     print("invalid operation")


#leap_year
# year= int(input("enter a leap year"))
# if(year%400==0 and year%4==0 or year%100!=0 ):
#     print("it is a leap year")
# else:
#     print("its not a leap year")

# ##primeno.
# for num in range(2,101):
#     for i in range(2,num):
#         if(num%i==0):
#             break
#     else:
#         print(num,"it is a pn")

####quadratic equation
# a = int(input("enter a no."))
# b = int(input("enter a no."))
# c = (2*a*a)+3*b
# print(c)



#reverse of  a string
# var = "python"
# print(var[::-1])
# for i in range (len(var)-1,-1,-1):
#     print(var[i],end=" ")


##### list
# # list_var = [2 , 83 , 324 , 23 ,334,32,123,"abc","xyz"]
#  print(list_var)
# list_var.append(15)
# print(list_var)
# list_var.insert(2,"python")
# print(list_var)
# print(list_var(3))
# print(list_var(-3))
# print(len(list_var))
# print(list_var[20])
# new_list=list_var[:20]
# print(new_list)

 ###tuples
# tuple_var = (2 , 83 , 324 , 23 ,334,32,123,"abc","xyz")
# print(tuple_var)
# print(len(tuple_var))

###dictionary
# dict_var ={
#     "name" : "vivek",
#     "phone" : 9897136104,
#     "height": 5.3,
#     "married" : False
# }
# print(dict_var)
# print(dict_var["name"])
# dict_var["name"]="viv"
# dict_var["city"]="dehradun"
# print(dict_var)

 ###list comprehension
# even_numbers = (x for x in range(0,100) if(x%2==0))
# print(even_numbers)
# list_var = [int(input("enter any no.")) for i in range(10)]
# print(list_var1)
# list_str = [input("enter any str").split(".")]
# print(list_str)

####calender
# import calendar
# a = calendar.month(2019,6)
# print(a)

####taking input and do basic calculations by functions
# a = int(input("enter a value"))
# b = int(input("enter a value"))
# d = int(input("1.addition 2.sub 3.mul 4.div"))
# def fuct1(a,b):
#     c = a+b
#     print(c)
# def fuct2(a,b):
#     c=a-b
#     print(c)
# def fuct3(a,b):
#     c= a*b
#     print(c)
# def fuct4(a,b):
#     c = a/b
#     print(c)
# if(d==1):
#     fuct1(a,b)
# elif(d==2):
#     fuct2(a,b)
# elif(d==3):
#     fuct3(a,b)
# elif(d==4):
#     fuct4(a,b)
# else:
#     print("invalid option")

####recurssion factorial
# def fact(n):
#     if(n==1):
#         return n
#     else:
#         return n*fact(n-1)
# n = int(input("enter a no."))
# if(n<0):
#     print("not possible for negative no")
# elif(n==0):
#     print("not done")
# else:
#     print("the factorial of n is",fact(n))


#####n inputs and print list
# n = int(input("how mny age u want to check:"))
# list_age = []
#
# for i in range(n):
#     age = int(input("enter the age"))
#     list_age.append(age)
#     if(age<18):
#         print("noteligible")
#     else:
#         print(" eligible")
# print(list_age)


# ####dictionary
# n = int(input("how mny age u want to check:"))
# dict = {}
# for i in range(n):
#     age = int(input("enter the age"))
#
#     if(age<18):
#         dict.update({age:"noteligible"})
#     else:
#         dict.update({age:"eligible"})
# print(dict)

#####no. of words
# list_para = []
# a = input("enter a para").split(" ")
# list_para.append(a)
# print(len(a))

#####sets
# colour1 = set ([ "yellow" ,"white" ,"blue" ,"green","red" ,"green" ,"orange"])
# colour2 = set ([ 'yellow' ,"white" ,"blue" ,"green" ])
# print(colour1 - colour2)


# #####max min without built in
# list = [int(input("enter nos")) for i in range(0,6)]
# print(list)
# max=list[0]
# min =list[0]
# for i in range(1,6):
#     if(list[i]>max ):
#         max=list[i]
# print("maximum is",max)
# for i in range(1,6):
#     if(list[i]<min):
#         min=list[i]
# print("minimum is",min)


####create a list comprehension of an range
# list = [i for i in range(0,10)]
# print(list)

###insert in a line
# list = [int(input("enter nos")) for i in range(0,4)]
# print(list)

##dance combinations
# girls = ["deepika","preeti","simmi","sona"]
# boys = ["viv","sid","umesh","ojas"]
# combinations=[]
# for i in girls:
#     for j in boys:
#         partner = (i,j)
#         combinations.append(partner)
# print(combinations)


###lambda function
# list1 = [38, 46, 45, 22, 29, 88]
# new_list=list(filter(lambda x: x>30,list1))
# print(new_list)

# ###
# dictionary = {
#     0: "sunday",
#     1: "monday",
#     2: "tuesday",
#     3: "wednesday",
#     4: "thursday",
#     5: "friday",
#     6: "saturday"
# }
# list_weeks = [7,2,8,1,3,1,4,5,0,2,1,0,4]
# list_weeks = list(map(lambda x: dictionary.get(x,"notfound"),list_weeks))
# print(list_weeks)

#######
# from functools import reduce
# list_var = [9,3,2,43,9,232,34]
# multiplication = reduce(lambda x,y:x*y,list_var)
# print("mul result is:",multiplication)
# #########


# list1= [input("enter values") for i in range(0,11)]
# integer_num = list(map(lambda x: int(x),list1))
# from functools import reduce
# sum = reduce(lambda x,y:x+y,integer_num)
# print("sum is:",sum)


######list greater than median of list(inbuilt statistics)
# import statistics
# list_var = [input("enter values") for i in range(0,5)]
# list_var.sort()
# print(list_var)
# s=statistics.median(list_var)
# print("median of data is,",s)
# new_list = list(filter(lambda x:x>s,list_var))
# print(new_list)


# ##############
# first =  int(input("enter first no."))
# second = int(input("enter second no."))
# third = int(input("enter third no."))
# answer =int(input("enter ans of your choice"))
# possile_results = []
# for i in range(0,first+1):
#     for j in range(0,second+1):
#         for k in range(0,third+1):
#             sum = i+j+k
#             if(sum<=answer):
#                 result = [i,j,k]
#                 possile_results.append(result)
# print("possible combinations are",possile_results)