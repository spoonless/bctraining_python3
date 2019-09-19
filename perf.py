"""
Un module pour aider à mesurer les performances
"""

def bench(f):
    import time
    """@bench : un décorateur pour mesurer le temps d'exécution d'une fonction"""
    def decorateur(*args, **kwargs):
        start = time.perf_counter()
        r = f(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"Temps d'exécution : {end}")
        return r

    return decorateur

