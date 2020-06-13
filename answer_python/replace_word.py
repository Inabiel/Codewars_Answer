def alphabet_position(text):
    text = text.lower()
    word = " ,.':`!@#$%^&*()1234567890-_=+"
    res = [str(ord(i) - 96) for i in text if i not in word]
    return " ".join(res)
