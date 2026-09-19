# RUN THIS CODE TO LOAD THE PLOTTING FUNCTION #
# we'll use matplotlib to plot #
import matplotlib.pyplot as plt

'''
This function takes in an array of tuples to plot. Tuples are defined using (x, y, z )
The tuple values for x will be an array of values to use for the x axis
The tuple values for y will be an array of values to use for the y axis
the z value will be an option string that can be used to set the color, if left off a random color will be chosen
'''
def plotValues(plots: list[tuple], x_min = 0, x_max = 10000000, y_min = 0, y_max = None):
  plt.gca().set_xlim(x_min, x_max)
  plt.gca().set_ylim(y_min, y_max)
  for plot in plots:
    plt.plot(plot[0], plot[1], plot[2] if len(plot) > 2 else '')
  plt.show()

# this library will allow access to a number of mathematical functions #
import math

# this array stores some increasing values of n #
n = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000, 500000000, 1000000000, 5000000000, 10000000000, 50000000000]

# these lines perform various mathematical operaitons on the n array #
# DO NOT CHANGE THESE LINES #
n_log_ = [i/100 * math.log2(i) for i in n]
log_ = [5e8*math.log2(i) for i in n]
n_ = [i for i in n]

# UPDATE THE MATHEMATICAL FUNCTION IN THE LINE BELOW TO USE YOUR OWN MATHEMATICAL OPERATION #
# USE A DIFFERENT OPERATION THEN USED ABOVE #
# THE VARIABLE i REPRESENTS THE VALUE BEING OPERATED ON, DO NOT ALTER THE for i in n STATEMENT #
#your_function = [ ( ##ENTER YOUR CODE BETWEEN THE ( ) HERE## ) for i in n]

plotValues([
    (n, log_, 'g'),
     (n, n_log_, 'b'),
      (n, n, 'y'),
       #(n, your_function, 'r') # UNCOMMENT THIS LINE ONCE YOU HAVE CREATED yourfunction LOGIC #
       ], x_min = -5e9, x_max = 5e10, y_max = 5e10)

# import numpy for easier creation of the array #
from numpy import random

'''
This Function will be used to create a number of arrays containing random ints
We will use the array to test the run time complexity of a number of algorithms
'''
def createRandomArray(size: int, lowerBound: int = 0, upperBound: int = 65536) -> list[int]:
  # return an empty array if the size is not a positive number or upperBound is not >= lowerBound #
  if (size <= 0 or lowerBound > upperBound):
    return []
  # we'll use numpy to simplify the array creation
  return random.randint(lowerBound, upperBound, size)

# These arrays should always be empty
print("This array should be empty ", createRandomArray(0))
print("This array should be empty ", createRandomArray(-1))

# This array should have one value that 'should' change every time. It's random so the value might be the same across some executions #
print("This array should contain one element ", createRandomArray(1))

# Use the createRandomArray function, defined above, to generate the appropriate array for the variables below.
# Each variable is accompanied by a comment describing what the properties of the resulting array should be

# This is an array of arrays that will make it easier to run the functions on all of the data sets together
array_sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000] # these are the sizes of the unsorted arrays #
unsorted_arrays = [None] * 7

# 10 element array, with values between 0 and 65536
unsorted_arrays[0] = createRandomArray(10) # this is an example of how createRandomArray should be called

# 100 element array, with values between 0 and 65536
unsorted_arrays[1] = ##ADD CALL TO createRandomArray HERE ###

# 1000 element array, with values between 0 and 65536
unsorted_arrays[2] = ##ADD CALL TO createRandomArray HERE ###

# 10000 element array, with values between 0 and 65536
unsorted_arrays[3] = ##ADD CALL TO createRandomArray HERE ###

# 100000 element array, with values between 0 and 65536
unsorted_arrays[4] = ##ADD CALL TO createRandomArray HERE ###

# 1000000 element array, with values between 0 and 65536
unsorted_arrays[5] = ##ADD CALL TO createRandomArray HERE ###

# 10000000 element array, with values between 0 and 65536
unsorted_arrays[6] = ##ADD CALL TO createRandomArray HERE ###

# If you want to check your array sizes, I would not recommend printing them, since some are very very large, instead you can check the len #
print([len(i) for i in unsorted_arrays])

import time

'''
This function takes in the function to profile, the array of input arrays, and an iterations
value that indicates how many times the function should be run. It's usually a good idea to
run profiing code multiple times to get an average time elapsed
'''
def calculateFunctionRunTimes(func, arrayOfArrays: list[list[int]], iterations: int = 5) -> list[int]:
  # confirm the input is as expected #
  if func and len(arrayOfArrays) > 0:
    # initial the return array #
    runTimes = []

    # perform the iterations loop, for each iteration, perform the function and add up the run times #
    # it's presumed that the passed in func will take an array of ints as an argument
    # we're not concerned with the result of func, at least not for now
    for array in arrayOfArrays:
      iterationTime = 0.0
      for i in range(iterations):
        start = time.time()
        func(array)
        iterationTime += time.time() - start
      # store the average time across all iterations #
      runTimes.append(iterationTime/iterations)

    # return the array of run times #
    return runTimes

  # This is the fallback return for when the inputs were not valid #
  return None

'''
This function will return the specified index from the passed in array
or by default, return the element at the last index
If the array is empty, it'll return None
'''
def returnIndex(arrayOfInts: list[int], index: int = -1) -> int:
  if len(arrayOfInts) > 0:
    if index > -1:
      return arrayOfInts[index]
    return arrayOfInts[len(arrayOfInts) - 1]

  # the input array had no elements, so no value could be selected #
  return None

runTime_returnRandomIndex = calculateFunctionRunTimes(returnIndex, unsorted_arrays, 1000)

# This block calculates an average value to set a better y axis limit
avg_value = 0
for i in runTime_returnRandomIndex:
  avg_value += i
avg_value /= len(runTime_returnRandomIndex)
######

print(runTime_returnRandomIndex)

# plot our index run times #
plotValues([(array_sizes, runTime_returnRandomIndex)], x_max = max(array_sizes), y_max = avg_value*10)

runTime_pythonTimSort = calculateFunctionRunTimes(sorted, unsorted_arrays , 1)

print(runTime_pythonTimSort)

# PLOT THE RUN TIMES OF THE sorted FUNCTION #
plotValues([ (array_sizes, runTime_pythonTimSort ), (array_sizes, [max(runTime_pythonTimSort) * i/max(array_sizes) for i in array_sizes], 'r') ], x_max = max(array_sizes), y_max = max(runTime_pythonTimSort))

sorted_arrays = []
for array in unsorted_arrays:
  sorted_arrays.append(sorted(array))

'''
This function chooses the last value in the array and then performs a search to find that value
It will return true if the value was found or false if it was not
'''
def iterativeSearch(array):
  value = array[len(array)-1]
  for i in array:
    if value == i:
      return True
  return False

# Executes the iterativeSearch function on our input arrays #
runTime_pythonIterativeSearch = calculateFunctionRunTimes(iterativeSearch, sorted_arrays, 1)

print(runTime_pythonIterativeSearch)

# CALL THE plotValues FUNCTION USING THE array_sizes AND runTime_pythonIterativeSearch ARRAYS #
# YOU DO NOT NEED TO MODIFY THE x_max or y_max VALUES, ONLY UPDATE THE VALUES INSIDE THE [.( ) ] #
plotValues([('''REPLACE VALUE HERE''' , '''REPLACE VALUE HERE'''), (array_sizes, [max(runTime_pythonIterativeSearch) * i/max(array_sizes) for i in array_sizes], 'r')], x_max = max(array_sizes), y_max = max(runTime_pythonIterativeSearch))

'''
This function definition takes in an input array of ints. You are to add logic to perform an operation
on the array. It could perform a mathematical operation, it could look for a value using a different method than the itertive search.
It could reverse the array. The choice of operation is up to you
'''
def yourArrayOperation(array: list[int]):

  # ADD YOUR LOGIC TO PERFORM AN OPERATION ON THE ARRAY #

  return

# CALL the calculateFunctionRunTimes FUNCTION BELOW. PASS IN EITHER THE unsorted_arrays OR sorted_arrays VALUES AS NEEDED BY YOUR FUNCTION LOGIC, YOU CAN SET ITERATIONS TO 1 #

# PRINT OUT YOUR RUN TIMES RESULTS, THE RUN TIME RESULTS NOT THE RESULT OF YOUR FUNCTION #
