#Simple Try - except
try:
    a = 10/0
    print(a)
except Exception as e:
    print('Err>', e)

else:
    print('No Error')
