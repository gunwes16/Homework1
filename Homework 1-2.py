#!/usr/bin/env python
# coding: utf-8

# 1. Print out your favorite color and write comment about what you are doing above the code.

# In[19]:


# I put in the color and the quotations around it
print('green')


# 2. Print the sumation of numbers 1 through 10

# In[18]:


print(1+2+3+4+5+6+7+8+9+10)


# 3. Print what 2 to the 8th power is.

# 2**8

# 4. Print the remainder of 100 divided by 11. 

# In[17]:


print(100 % 11)


# 5. What is the result of adding strings: 20, 8, 77?

# In[16]:


result = 20+8+77
print(result)


# 6. Print out 100 divided by 5

# In[15]:


print(100/5)


# 7. What is the difference (subtraction) between 10/4 and 10//4?  Print out the result

# In[20]:


result=10/4 - 10//4
print(result)


# 8. Create a variable called height and store your height value there.
# Print a sentence describing your height and use the variable in the sentence as well.

# In[21]:


height = 'six foot'
print('I am' + " " + height)


# 9. Print the same information as exercise 8 using a formatted string. 

# In[22]:


height = 'six foot'
print("Hello I am {}!". format(height))


# 10. Use two different (single and double) quotes in a string to print out a sentence

# In[23]:


first_name = "Stevie"
last_name = 'Wonder'
print('The main character is first_name last_name.')


# 11. Print out Hello World! 7 times each on a new line using only one line of code.

# In[24]:


words = ["Hello world !"]
print(words * 7)


# 12. Write a code to get two integers from a user. Then print out their summation, subtraction, multiplication, and division.

# In[25]:


x = int("12")
y = int("5")
z = x + y
print(z)
z= x - y
print(z)
z= x * y
print(z)
z= x/y
print(z)


# In[ ]:





# 13. You and your collegue have been tasked to write a code to get 5 numbers from a user and then print out their summation and average in a formatted string.  Your partner wrote codes below.  Now it is up to you to fix all errors.

# In[ ]:


prompt = f"Enter a number: "

numb1 = input("7")
numb2 = input("6 ")
numb3 = input("5 ")
numb4 = input("4")
numb5 = input("3")

total = numb1 + numb2 + numb3 + numb4 + numb5
avg = total / 5

print("{numb1} + {numb2} + {numb3} + {numb4} + {numb5} = {total}")
print("average is {total}")


# In[ ]:





# 14. You and your partner have been assigned to a project to write a program to calculate the amount of runoff rain on a roof from any given rainfall.  
# 
# You and your partner have figured out that to calculate the runoff from any given rainfall. 
# 
# You need to take the dimensions of the footprint of the roof and <b>convert them to inches</b> (ex - a 50' x 20' roof is 600" x 240"). The dimensions should be user submitted. 
# 
# Then, multiply the roof dimensions by the number of inches of rainfall. As an example, 600" x 240" x 1" = 144,000 cubic inches of water for an inch of rainfall. Finally, divide that result by 231 to get the number of gallons (because 1 gallon = 231 cubic inches; 144,000/231 = 623.38).
# 
# Your partner started coding before getting sick and it is up to you to finish the program.

# In[1]:


print("\nRainfall Calculation ***\n")

width = int("400 ")
length = int("600")
rain = int("2")

area = (width * length * rain)
print(area)
print(area/231)


# In[ ]:





# 15. A program is required to get a customer’s name, a purchase amount and a discount rate (in %). The program must compute the discount amount, sales tax (6%) and the total amount due. Using one print statement, print the customer’s name, purchase amount, discount amount, sales tax and total amount due in friendly format.

# In[14]:


tax = 0.055

sub_total = 10.00 * 7
sales_tax = 70 * 0.06
discount = sub_total * 0.05
total = sub_total + 0.06

print(f"10:\t\t${10.00:.2f}")
print(f"Quantity:\t{7}")
print("-" * 30)
print(f"Subtotal:\t${sub_total:.2f}") 
print(f"Sales Tax:\t${sales_tax:.2f}")
print("=" * 30)
print(f"Total:\t\t${total:.2f}")


# In[ ]:





# In[ ]:




