# List

## I Presentation

List is a standard python variable type.

## II Generals Informations

### Links

- [Python official documentation](https://docs.python.org/3/tutorial/datastructures.html "official documentation for python list")

### Install

Already install in python.

## III Use

### Basic use

- #### Define a list

```python
empty_list = []
random_list = [5, 1, "hello"]
number_list = list(range(start_value, end_value, step_value))
```
The third method allows to create a list from *start_value* to *end_value* with
a step of *step_value*. To note that *end_value* isn't in list.

- #### Access to value in list

All elements of a list are indexed by a positive number. 0 for the first, 1 to the second and etc.

```python
random_list = [5, 8, 3, 'hello']

first_value = random_list[0] # first_value is 5
end_value = random_list[3] # end_value is 'hello'
```

⚠ if you try to access a value not present in the list, it will generate an **IndexError**.

Python allows access to the last value of a list without going through their indexes.to do this, we look for the index of the nth value starting from the end.

For example, -5 is for the 5th value from the end.

```python
last_value = random_list[-1]
second_last_value = random_list[-2]
n_th_from_end_value = random_list[-n]
```

- #### Get length of list

To avoid the IndexError, we can access the size of a list .

```python
length_of_list = len(list)
```

- #### Add value

To add a value to the end of the list, we use the `append(value)` function.

```python
random_list = [1, 2, 3, 4]
random_list.append(9) # random_list is [1, 2, 3, 4, 9]
```

To add a value to a precise index of the list, we use the `insert(index, value)` function.

```python
random_list = [1, 2, 3, 4]
random_list.insert(1, 9) # random_list is [1, 9, 2, 3, 4]
random_list.insert(9, 'a') # random_list is [1, 9, 2, 3, 4, 'a']
```

To add multiple value to the end of the list, we use the `extend(list_of_value)` function.

```python
random_list = [1, 9, 5]
random_list.extend([5, 6, 1]) # random_list is [1, 9, 5, 5, 6, 1]
```

- #### Remove value

To delete a specific value in a list, use multiple functions.

1. `del list[index]` : remove in list the value with this index
2. `list.pop(index)` : same, but if index is not define, remove the last value of list
3. `list.remove(value)` : remove this first occurrence of this value in list, raises **ValueError** if value isn't in list
4. `list.clear()` : remove all elements from a list

```python
random_list = [1, 3, 5, 7 ,9]
del random_list[2] # random_list is [1, 3, 7, 9]
random_list.pop(0) # random_list is [3, 7, 9]
random_list.remove(9) # random_list is [3, 7]
random_list.clear() # random_list is []
```

- #### Other operation

To get the index of value in list, use `list.index(value)`:

⚠ This function raises **ValueError** if isn't in list.

```python
random_list = [1, 5, 9]
index = random_list.index(5) # return 1
```

To count the number of occurrence of one value, use `list.count(value)`:

```python
random_list = [1, 5, 9, 5]
number_of_5 = random_list.index(5) # return 2
number_of_7 = random_list.index(7) # return 0
```

To reverse the list, use `list.reverse()`:

```python
random_list = [1, 2, 8, 4, 3]
random_list.reverse() # random_list is [3, 4, 8, 2, 1]
```

- #### Compare list

To compare to list, we use the == operation:

```python
if list_1 == list_2:
    # True segment
else:
    # False segment
```

To test if value is in list, use `in`:
```python
if value in list:
  # True segment
else:
  # False segment
```

### List as object

The variable does not contain the list itself but the address in the memory of
this one. This leads to particular effects when used.

For example:
```python
first_list = [1, 5, 6, 8]
second_list = first_list
second_list.append(9)

# here, second_list = [1, 5, 6, 8, 9] and first_list = [1, 5, 6, 8, 9]
```
To actually copy a list, ie to avoid these side effects, you can use the
`list.copy()` function.
```python
first_list = [1, 5, 6, 8]
second_list = first_list.copy()
second_list.append(9)

# here, second_list = [1, 5, 6, 8, 9] and first_list = [1, 5, 6, 8]
```
### Concatenated list
List concatenation create a new separate list for each operation you do.
