#Count Method
#short Method
#shorted Function
#Reverse Method
#copy Method
#Clear Method

#Copy Method
List=["Apple","Banana","Mango","Orange","Apple"]
List2=[6,9,2,7,1,5]
print(List.count("Apple"))

#Shorted Function
print(sorted(List)) 
print(sorted(List2))
#Sorted function does not change the Variable data only print shorted
 
#sort method
print(List.sort())
print(List2.sort())
print(f"Permanent Change Variable data {List} And {List2}")

#Reverse Method
#Only data Reverse
List.reverse() #Always Use Outside Print
print(List)

#Clear All data from list permanent
List.clear() #Always Use Outside Print
print(List)

#Copy List Method
List3=List2.copy() 
print(List3)