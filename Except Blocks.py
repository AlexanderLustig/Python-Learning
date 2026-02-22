
try:
    f = open('test.txt')
except FileNotFoundError:
    print('Sorry file not found')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')