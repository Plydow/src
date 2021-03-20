# Matplotlib

## I Presentation

Matplotlib is a library to show graphic and illustrate mathematical result.

## II Generals Informations

### Links

- [matplotlib official docs](https://matplotlib.org/ "matplotlib official docs")
- [Github](https://github.com/matplotlib/matplotlib "Official Github")

### Install

With pip:

```bash
python -m pip install matplotlib
```

## III Use

### Importation

```python
import matplotlib.pyplot as plt
```

### Show graphic

Display on graph of value from list_y in function of list_x

```python
plt.plot(list_x, list_y, args) # define value for a graph
plt.show() # display this graph
```

the function plot admits different arguments args:

- label (string) : name display on graph for this curve
- linestyle ['-', '--', '-.', ':'] : the way the curve is displayed
- color (matplotlib color) : the color of the curve
- alpha (float between 0 and 1) : the transparency of the curve

the function display the graph and stop execution while the window is open

### Customization

Define the name of axis

```python
plt.xlabel(string) # define the name of x axis
plt.ylabel(string) # idem for y axis
plt.legend()
```

### Multiple Graphic in One Window

Display multiple graphic in one window

```python
plt.subplot(number)
{
    # code for the first graphic
}
plt.subplot(number)
{
    # code for the second graphic
}
plt.legend()
plt.show()
```

For the number, it's in the form of 3 digits, the number of row, the number of column and the index of graph. for exemple:

- 131: 1 line, 3 column, and the first graph
