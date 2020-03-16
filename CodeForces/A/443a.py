test = input()
print(str(len({i for i in test[1:len(test)-1].split(', ') if i != ''})))
