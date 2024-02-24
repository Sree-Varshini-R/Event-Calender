import calendar
e={}

def create_events():
    
    ch=input('want to add events(y/n):')
    
    if ch=='y':
        A=int(input('how many:'))
        
        for i in range(0,A):
            em=int(input('enter event month:'))
            ed=int(input('enter event date:'))
            en=input('enter event name:')
            et=input('enter event time:')
            e[em]=ed,en,et
            print('Event is added')
print(e)
create_events()

def show_months_events():
    a= int(input('enter a year:'))    

    for i in range(1,13):
        c=calendar.TextCalendar(calendar.SUNDAY)
        str= c. formatmonth(a,i)
        print(str)

        print('\n')
        for I in e:
            if I==i:
                print('EVENT DATE:',e.get(I)[0],'\n', 'EVENT NAME:',e.get(I)[1],'\n', 'EVENT TIME:',e.get(I)[2])

show_months_events()
