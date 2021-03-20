"""
Nulba est un mobule d'optimisation de python permetant une forte acceleration
de l'execution du script.
"""
#python version
3.8 and +

#install
python -m pip install numba

#docs
https://numba.readthedocs.io/en/stable/

#use
"ne fonctionne que sur des fonctions (doit pouvoir faire plus mais pas étudié)"

from numba import jit

@jit(nopython=True)
def function(args):
    'your code here'
    pass

"[w]: la première fois que la fonction est appelée, le temps d'execution est "
"plus long."
