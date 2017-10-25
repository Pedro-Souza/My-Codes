from typing import List


numbers = List[float]


def somar(multi: float, lista: List) -> List:
    return [multi * i for i in lista]


print(somar(2.0, [1,2,3,4]))