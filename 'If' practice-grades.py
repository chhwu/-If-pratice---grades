grade = int(input('Please enter you grade: '))
if grade >= 95:
    print('EXCELLENT, you got an A+ !')
elif 90 <= grade < 100:
    print('A')
elif 80 <= grade < 90:
    print('B')
elif 70 <= grade < 80:
    print('C')
elif 60 <= grade < 70:
    print('D')
else:
    print('Fail')