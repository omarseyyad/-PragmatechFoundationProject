emr=input('Emri daxil edin: ')
def hesabla():
    a=5
    b=6
    if emr=='+':
        return a+b
    elif emr=='-':
        return a-b
    elif emr=='*':
        return a*b
    elif emr=='/':
        return a/b
    else:
        return 'Sehv emelyat'