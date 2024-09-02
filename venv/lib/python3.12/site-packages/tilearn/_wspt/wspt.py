import tilearn as tl

def custom_wspt(a, plan_time):
    a = tl.factor_data(a, plan_time)
    a.sort(key=lambda x: x[6], reverse=True)
    return a