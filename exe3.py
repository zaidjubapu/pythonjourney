'''
You visit a restaurant called CodeWithHarry and food items in this restaurant are sorted based on their amount of calories. You have to reverse this list of food items containing their calories.

You have to use following three methods to reverse a list:

• Inbuilt method of python
• Listname[::-1] slicing trick
• Swapping first element with last one and second element with second last one and so on….
Input:
Take a list as an input from the user.
[5,4,1]

Output:
[1,4,5]
[1,4,5]
[1,4,5]
All the three methods give same results!
'''
# dishes=[i for i in input("enter the list of items with space").split()]
dishes=[5,4,33,54,3,23,44]
item=dishes.copy()
print(item.reverse()) #.reverse will not give any return value so it will give none
print(item)
# print(dishes.reverse())
print(dishes[::-1])
# dishes[0]=dishes[3]
print(dishes)
length=len(dishes)
z=length//2
print(z)
for i in range(z):
    dishes[i],dishes[length-1]=dishes[length-1],dishes[i]
    length=length-1
print(dishes)