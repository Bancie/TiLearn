import tilearn as tl


def wspt(a, plan_time):
    a = tl.factor_data(a, plan_time)
    a.sort(key=lambda x: x[5], reverse=True)
    return a