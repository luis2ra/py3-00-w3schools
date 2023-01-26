# @author: https://github.com/luis2ra from https://www.w3schools.com/python/python_ml_mean_median_mode.asp

'''
Machine Learning - Mean Median Mode


Mean, Median, and Mode

What can we learn from looking at a group of numbers?

In Machine Learning (and in mathematics) there are often three values that interests us:

Mean - The average value
Median - The mid point value
Mode - The most common value

Example: We have registered the speed of 13 cars:

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

What is the average, the middle, or the most common speed value?

'''

print("Mean")

'''
Mean

The mean value is the average value.

To calculate the mean, find the sum of all values, and divide the sum by the number of values:

(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77

'''
import numpy

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.mean(speed)

print(x)


'''
Median

The median value is the value in the middle, after you have sorted all the values:

77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111

It is important that the numbers are sorted before you can find the median.

'''
print("Median")

y1 = numpy.median(speed)

print(y1)

# If there are two numbers in the middle, divide the sum of those numbers by two.
speed2 = [99, 86, 87, 88, 86, 103, 87, 94, 78, 77, 85, 86]

y2 = numpy.median(speed2)

print(y2)


'''
Mode

The Mode value is the value that appears the most number of times:

99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86

'''
print("Mode")

from scipy import stats

speed3 = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

z = stats.mode(speed3, keepdims=False)  # The mode() method returns a ModeResult object that contains the mode number (86), and count (how many times the mode number appeared (3)).

print(z)
