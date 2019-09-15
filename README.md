# Data Analysis Library Sharks

This repository contains a detailed note of a new data analysis library Sharks.



## Objectives

Sharks :

* Has A DataFrame class with data stored in numpy arrays
* Can Select subsets of data with the brackets operator
* Can Use special methods defined in the Python data model
* Have a nicely formatted display of the DataFrame in the notebook
* Can Implement aggregation methods - sum, min, max, mean, median, etc...
* Can Implement non-aggregation methods such as isna, unique, rename, drop
* Can Group by one or two columns
* Have methods specific to string columns
* Can Read in data from a comma-separated value file



## Functionalities of Sharks


### 1. DataFrame constructor input types

Our DataFrame class is constructed with a single parameter.

Specifically, input types must qualify the following:

* Sharks will raise a `TypeError` if `data` is not a dictionary
* Sharks will raise a `TypeError` if the keys of `data` are not strings
* Sharks will raise a `TypeError` if the values of `data` are not numpy arrays
* Sharks will raise a `ValueError` if the values of `data` are not 1-dimensional




### 2. Array lengths

We are now guaranteed that `data` is a dictionary of strings mapped to one-dimensional arrays. Each column of data in our DataFrame must have the same number of elements. 

### 3. Convert unicode arrays to object

Whenever you create a numpy array of Python strings, it will default the data type of that array to unicode. Take a look at the following simple numpy array created from strings. Its data type, found in the `dtype` attribute is shown to be 'U' plus the length of the longest string.

```python
>>> a = np.array(['cat', 'dog', 'snake'])
>>> a.dtype
dtype('<U5')
```

Unicode arrays are more difficult to manipulate and don't have the flexibility that we desire. So, if our user passes us a Unicode array, we will convert it to a data type called 'object'. This is a flexible type and will help us later when creating methods just for string columns. Technically, this data type allows any Python objects within the array.


### 4. Find the number of rows in the DataFrame with the `len` function

The number of rows are returned when passing a pandas DataFrame to the builtin `len` function.


### 5. Return columns as a list

 `df.columns` will return a list of the column names.


### 6. Set new column names

we can assign all new columns to our DataFrame by setting the columns property equal to a list. A example below shows how you would set new columns for a 3-column DataFrame.

```python
df.columns = ['state', 'age', 'fruit']
```

Also Sharks will raise errors if the data that is inserted is invalid.

* Sharks will Raise a `TypeError` if the object used to set new columns is not a list
* Sharks will Raise a `ValueError` if the number of column names in the list does not match the current DataFrame
* Sharks will Raise a `TypeError` if any of the columns are not strings
* Sharks will Raise a `ValueError` if any of the column names are duplicated in the list



### 7. The `shape` property

The `shape` property will return a two-item tuple of the number of rows and columns. 


### 8. Visual HTML representation in the notebook with the `_repr_html_` method


The `_repr_html_` method is made available to developers by iPython so that your objects can have nicely formatted HTML displays within Jupyter Notebooks. Read more on this method [here in the iPython documentation][12] along with other similar methods for different representations.


### 9. The `values` property

`values` is a property that returns a single array of all the columns of data. 


### 10. The `dtypes` property

The `dtypes` property will return a two-column DataFrame with the column names in the first column and their data type as a string in the other. Use 'Column Name' and 'Data Type' as column names.


### 11. Select a single column with the brackets

In Sharks, you can select a single column with `df['colname']`.

### 12. Select multiple columns with a list

Sharks will also be able to select multiple columns if given a list within the brackets. For example, `df[['colname1', 'colname2']]` will return a two column DataFrame.

### 13. Boolean Selection with a DataFrame

In Sharks, you can filter for specific rows of a DataFrame by passing in a boolean Series/array to the brackets. For instance, the following will select only the rows such that `a` is greater than 10.

```python
>>> s = df['a'] > 10
>>> df[s]
```


### 14. Check for simultaneous selection of rows and columns



### 15. Select a single cell of data

Sharks can select a single cell of data with `df[rs, cs]`. We will assume `rs` is an integer and `cs` is either an integer or a string.


### 16. Simultaneously select rows as booleans, lists, or slices

Sharks can select rows and columns simultaneously with `df[rs, cs]`. We will allow `rs` to be either a single-column boolean DataFrame, a list of integers, or a slice. 

### 17. Simultaneous selection with multiple columns as a list


### 18.  Simultaneous selection with column slices

Sharks will allow  columns to be sliced with either strings or integers. The following selections will be acceptable.


### 19. Tab Completion for column names


### 20. Create a new column or overwrite an old column


### 21. `head` and `tail` methods

The `head` and `tail` methods each accept a single integer parameter `n` which is defaulted to 5. 

### 22. Generic aggregation methods

Sharks can implement several methods that perform an aggregation. These methods all return a single value for each column. The following aggregation methods are defined.

* min
* max
* mean
* median
* sum
* var
* std
* all
* any
* argmax - index of the maximum
* argmin - index of the minimum


### 23. `isna` method

The `isna` method will return a DataFrame the same shape as the original but with boolean values for every single value. Each value will be tested whether it is missing or not. Use `np.isnan` except in the case for strings which you can use a vectorized equality expression to `None`.

### 24. `count` method

The `count` method returns a single-row DataFrame with the number of non-missing values for each column. You will want to use the result of `isna`.



### 25. `unique` method

This method will return the unique values for each column in the DataFrame. Specifically, it will return a list of one-column DataFrames of unique values in each column. If there is a single column, just return the DataFrame.



### 26. `nunique` method

Return a single-row DataFrame with the number of unique values for each column.


### 27. `value_counts` method


### 28. Normalize options for `value_counts`


### 29. `rename` method

The `rename` method renames one or more column names. Accept a dictionary of old column names mapped to new column names. Return a DataFrame. Raise a `TypeError` if `columns` is not a dictionary.



### 30. `drop` method

Accept a single string or a list of column names as strings. Return a DataFrame without those columns. Raise a `TypeError` if a string or list is not provided.



### 31. Non-aggregation methods

There are several non-aggregation methods that function similarly. All of the following non-aggregation methods return a DataFrame that is the same shape as the origin.

* `abs`
* `cummin`
* `cummax`
* `cumsum`
* `clip`
* `round`
* `copy`





### 32. Arithmetic and Comparison Operators

All the common arithmetic and comparison operators will be made available to our DataFrame. For example, `df + 5` uses the plus operator to add 5 to each element of the DataFrame. Take a look at some of the following examples:

```python
df + 5
df - 5
df > 5
df != 5
5 + df
5 < df
```


### 33. `sort_values` method

This method will sort the rows of the DataFrame by one or more columns. Allow the parameter `by` to be either a single column name as a string or a list of column names as strings. The DataFrame will be sorted by this column or columns.



### 34. `pivot_table` method


### 35. Reading simple CSVs

The `read_csv` function, will read in simple comma-separated value files (CSVs) and return a DataFrame.

