a = 0
b = 10

try:
    c = b / a
    print(c)
except Exception as e:
    print(e)
finally:
    print("block is completed")
