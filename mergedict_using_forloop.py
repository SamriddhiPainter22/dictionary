dict1 = { 'Alexa' : 27,      # given the first dictionary in key-value pairs  
            'lina Gomez' : 22,  
            'Jamey' : 29,  
            'Peter' : 30  
                        }   
dict2 = {  
            'Jas' : 19,      # given the second dictionary in key-value pairs  
            'Maya' : 26,  
            'Heena' : 30  
}                          
print("Before merging the two dictionary ")  
print("Dictionary No. 1 is : ", dict1) # print the dict1  
print("Dictionary No. 1 is : ", dict2)  # print the dict2  
  
dict3 = dict1.copy()  # Copy the dict1 into the dict3 using copy() method  
  
for key, value in dict2.items():  # use for loop to iterate dict2 into the dict3 dictionary  
    dict3[key] = value  
  
print("After merging of the two Dictionary ")  
print(dict3)    # print the merge dictionary  