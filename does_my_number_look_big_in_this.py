def narcissistic(value) -> int:
    val = [int(i) ** len(str(value)) for i in str(value)]
    return True if sum(val) == value else False
