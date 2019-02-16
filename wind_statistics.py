"""
Wind Statistics
----------------

Topics: Using array methods over different axes, fancy indexing.

1. The data in 'wind.data' has the following format::

        61  1  1 15.04 14.96 13.17  9.29 13.96  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71 16.88 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25  8.04  8.50  7.67 12.75 12.71

   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   locations in Ireland on that day.

   Use the 'loadtxt' function from numpy to read the data into
   an array.

2. Calculate the min, max and mean windspeeds and standard deviation of the
   windspeeds over all the locations and all the times (a single set of numbers
   for the entire dataset).

3. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds at each location over all the days (a different set of numbers
   for each location)

4. Calculate the min, max and mean windspeed and standard deviations of the
   windspeeds across all the locations at each day (a different set of numbers
   for each day)

5. Find the location which has the greatest windspeed on each day (an integer
   column number for each day).

6. Find the year, month and day on which the greatest windspeed was recorded.

7. Find the average windspeed in January for each location.

You should be able to perform all of these operations without using a for
loop or other looping construct.

Bonus
~~~~~

1. Calculate the mean windspeed for each month in the dataset.  Treat
   January 1961 and January 1962 as *different* months. (hint: first find a
   way to create an identifier unique for each month. The second step might
   require a for loop.)

2. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds across all locations for each week (assume that the first week
   starts on January 1 1961) for the first 52 weeks. This can be done without
   any for loop.

Bonus Bonus
~~~~~~~~~~~

Calculate the mean windspeed for each month without using a for loop.
(Hint: look at `searchsorted` and `add.reduceat`.)

Notes
~~~~~

These data were analyzed in detail in the following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.


See :ref:`wind-statistics-solution`.
"""

import numpy as np
from numpy import loadtxt

def read_from_file(file_name):
   array = np.array(np.loadtxt(file_name))
   return array

def all_time_value(data):
   print('all_time_min_value', data[:, 3:].min())
   print('all_time_max_value', data[:, 3:].max())
   print('all_time_mean_value', data[:, 3:].mean())
   print('all_time_std_value', data[:, 3:].std())

def third_ex(data):
   print('min_value_axis0',data[:, 3:].min(axis = 0))
   print('max_value_axis0',data[:, 3:].max(axis = 0))
   print('mean_value_axis0',data[:, 3:].mean(axis = 0))
   print('std_value_axis0',data[:, 3:].std(axis = 0))

def fourth_ex(data):
   print('min_value_axis1',data[:, 3:].min(axis = 1))
   print('max_value_axis1',data[:, 3:].max(axis = 1))
   print('mean_value_axis1',data[:, 3:].mean(axis = 1))
   print('std_value_axis1',data[:, 3:].std(axis = 1))

def fifth_ex(data):
   arg_max_value = data[:, 3:].argmax(axis = 1)
   return arg_max_value

def sixth_ex(data):
   _max = data[:, 3:].max(axis = 1)
   row = _max.argmax()
   print('Year:', data[row, 0])
   print('Month:', data[row, 1])
   print('Day:', data[row, 2])

def seventh_ex(data):
   average_value = np.average(data[:32:, 3:], axis=0)
   return average_value

def bonus_1(data):
   months = (data[:, 0] - 61) * 12 + data[:, 1] - 1
   months_values = set(months)
   month_mean = np.zeros(len(months_values))
   month_mean = np.array([data[months == month].mean() for month in months_values])
   return month_mean

def bonus_2(data):
   week_data = data[:52 * 7].reshape(-1, 7 * 12)
   print('min', week_data.min(axis = 1))
   print('max', week_data.max(axis = 1))
   print('mean', week_data.mean(axis = 1))
   print('std', week_data.std(axis = 1))




print(all_time_value(read_from_file('wind.data')))
print(third_ex(read_from_file('wind.data')))
print(fourth_ex(read_from_file('wind.data')))
print(fifth_ex(read_from_file('wind.data')))
print(sixth_ex(read_from_file('wind.data')))
print(seventh_ex(read_from_file('wind.data')))
print(bonus_1(read_from_file('wind.data')))
print(bonus_2(read_from_file('wind.data')))