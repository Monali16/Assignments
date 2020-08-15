while True:
    try:
        num = int(input('Please enter the number: '))
        print('Entered number is :', num)
    except:
        print('Please provide only four digit number')
        continue
    else:
        break

if(len(num)>4):
    print('Please lenght is too long')
elif(len(num)<4):
    print('Please length is too short.')