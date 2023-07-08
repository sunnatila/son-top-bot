from random import randint


def sonTopUser(son: int, result: dict) -> dict:
    result['urinish'] += 1
    if son == result['number']:
        result['ok'] = True
    elif son > result['number']:
        result['kattami'] = False
    elif son < result['number']:
        result['kattami'] = True
    return result


def generateNumber() -> int:
    return randint(1, 10)


def updateResult(result: dict) -> str:
    result['ok'] = False
    result['urinish'] = 0
    result['kattami'] = None
    result['number'] = generateNumber()
    return "Qiymatlar yangilandi!"


def compNumber(javop: str, result_bot: dict) -> dict:

    if javop == '+':
        result_bot['a'] = result_bot['number'] + 1
    elif javop == '-':
        result_bot['b'] = result_bot['number'] - 1
    elif javop == 't':
        result_bot['ok'] = True

    a = result_bot['a']
    b = result_bot['b']
    if a > b:
        result_bot['halol'] = False
        return result_bot

    result_bot['number'] = randint(a, b)
    result_bot['urinish'] += 1
    return result_bot


def newCompRandomNumber() -> int:
    return randint(1, 10)


def new_comp_number(result_bot: dict) -> str:
    result_bot['ok'] = False
    result_bot['urinish'] = 0
    result_bot['halol'] = True
    result_bot['number'] = newCompRandomNumber()
    return "Qiymat yangilandi"
