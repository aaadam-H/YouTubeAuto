import webbrowser as wb
import time
import sys

bukaYt = input('Do you want to launch Open YouTube automation?(y/n) ').lower() == 'y'
# time.sleep(3)
# sys.exit()

# print(bukaYt)
while True:
    try:
        if bukaYt:
            print('Opening YouTube')
            time.sleep(1)
            url = 'https://www.youtube.com/feed/subscriptions'
            wb.open(url)
            break
        else:
            print('Ending automation')
            time.sleep(1)
            break
    except:
        print('Error!')
    

