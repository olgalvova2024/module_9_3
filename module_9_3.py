first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(i)-len(j) for i,j in zip(first,second) if (len(i)-len(j)) > 0 )
print(list(first_result))
second_result = (True if ( len(first[i])-len(second[i]) == 0) else False for i in range(len(first)))
print(list(second_result))
