import tilearn as tl


def wspt(a):
    a = tl.factor_data(a)
    a.sort(key=lambda x: x[5], reverse=True)
    return a