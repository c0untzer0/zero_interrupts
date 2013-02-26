#!/usr/local/bin/python3

def to_fah(ctemp):
    ftemp=ctemp*9/5+32
    return ftemp
def to_cel(ftemp):
    ctemp=(ftemp-32)*5/9
    return ctemp

if __name__ =='__main__':
    print('Temperature converter\n')
    intemp=float(input('Enter a temperature: '))
    if intemp:
        while True:
            c=input('Convert to (f)ahrenheit or (c)elsius? ')
            if c=="f":
                print('{0:.2f} C = {1:.2f} F'.format(intemp,to_fah(intemp)))
                break
            elif c=="c":
                print('{0:.2f} C = {1:.2f} F'.format(intemp,to_cel(intemp)))
                break
            else:
                print('Please select a valid option')
        
