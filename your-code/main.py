#1. Import the NUMPY package under the name np.

import numpy as np
import random



#2. Print the NUMPY version and the configuration.

print(np.__version__)
print(np.show_config())

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.randint(1, 100, size=(2,3,5))


#4. Print a.

print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))

#6. Print b.


print(b)


#7. Do a and b have the same size? How do you prove that in Python code?

if a.shape > b.shape:
    print("A is bigger than b")
else:
    print("B is bigger than a")


#8. Are you able to add a and b? Why or why not?
try:
    np.add(a, b)
except ValueError:
    print("Operands could not be broadcast together with shapes (2,3,5) (5,2,3) ")


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.transpose(b, (1,2,0))
print(c)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a,c)



#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.


print(d)


#12. Multiply a and c. Assign the result to e.

e = np.multiply(a, c)

#13. Does e equal to a? Why or why not?

if np.array_equal(e, a):
    print("They are equal")
else:
    print("they are not equal")


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
print(np.amax(d))
print(np.amin(d))
print(np.mean(d))


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty(shape=((2,3,5)))



#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.


maxd_1 = np.amax(d)
mind = np.amin(d)
meand = np.mean(d)

array25 = np.full((2,3, 5), 25)
array0 = np.full((2,3, 5), 0)

g = np.where((d > mind) & (d < meand), array25, array0)


#If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.

array75 = np.full((2,3, 5), 75)

h = np.where((d > meand) & (d < maxd_1), array75, g)


#If a value equals to d_mean, assign 50 to the corresponding value in f.



#Assign 0 to the corresponding value(s) in f for d_min in d.
h[0][0][-1] = 0



#Assign 100 to the corresponding value(s) in f for d_max in d.
h[0][0][1] = 100


#In the end, f should have only the following values: 0, 25, 50, 75, and 100.
#Note: you don't have to use Numpy in this question.


#17
print(f)
print(h)