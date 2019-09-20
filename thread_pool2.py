"""
Exemple de programmation parallèle (lancement de plusieurs fonctions qui
produisent un résultat).

@author: David Gayerie
"""
from concurrent.futures import ThreadPoolExecutor

futures = []

with ThreadPoolExecutor(max_workers=5) as executor:
    futures.append(executor.submit(pow, 323, 1235))
    futures.append(executor.submit(pow, 125, 4569))
    futures.append(executor.submit(pow, 1, 2))
    futures.append(executor.submit(pow, 564, 365))

    for future in futures:
        print(future.result())
