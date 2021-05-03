#John Rick Santillan #1910045

def get_age():
    age=int(input())
    if age<18 or age>75:
        raise ValueError('Invalid age.')
    return age

def fat_burning_heart_rate(age):
    h_rate=(220-age)*.70
    return h_rate

if __name__=='__main__':
    try:
        age=get_age()
        print('Fat burning heart rate for a',age,'year-old:',"{:.1f}".format(fat_burning_heart_rate(age)),'bpm')
    except ValueError as ex:
        print(ex)
        print('Could not calculate heart rate info.\n')