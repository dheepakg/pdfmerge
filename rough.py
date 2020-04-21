file = {1:True,
        2:True}

print(file.values())

for i in file.values():
    if not i:
        print(False)
    else:
        print(True)


a = 'sds'
print(a.upper())


codecov --token=CODECOV_TOKEN
