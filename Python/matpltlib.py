"""
matplmotlib is a librairy to show graph in 2D, 3D,
animated graph
"""

#python version
3.0 and +

#install
python -m pip install matplotlib

#docs
https://matplotlib.org/

#use
"importation matplotlib"
import matplotlib.pyplot as plt

"show list_y in function of list_x"
plt.plot(list_x, list_y, args)

"""
args:
    -alpha: float
    -color: matplotlib color
    -label: string name of curbe
    -linestyle: ['-', '--', '-.', ':', ...]
"""

"show the graph"
plt.show() #this line show all graph and stop execution while the window is open

"name the axes"
plt.xlabel(string)
plt.ylabel(string)

"multiple graph on one window"
plt.subplot(number)
{
    code classic for this graph
}


"""
number:
    it's in the form of 3 digits, the number of row, the number of column and
    the index of graph.

    for exemple:
        131: 1 line, 3 column, and the first graph
"""
