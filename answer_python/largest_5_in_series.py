def solution(numberstr: int) -> int:
    values = [numberstr[i : i + 5] for i in range(len(numberstr) - 4)]
    values.sort()
    return int(values[-1])
