import tilearn as tl

def edd(a):
    a.sort(key=lambda x: x[3], reverse=False)
    return a