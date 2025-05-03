import time

def reset():
    q = str(input('Do you want to reset? y/n\n'))
    if q == 'y': main()
    else: quit()

def main():
    timer = int(input('Welcome to Countdown Timer. To start type time\n'))
    if timer < 0:
        print("You can't break time!")
        main()
    else:
        let = str(input('Now type letter using instruction!\ns - second\n m - minute\n h - hour\n'))
        if let == 's':
            print('Starting timer!')
            while True:
                print(timer)
                timer = timer-1
                if timer < 0:
                    print('Time is over!')
                    reset()
                time.sleep(1)

        if let == 'm':
            print('Starting timer!')
            timer = timer*60
            while True:
                print(timer)
                timer = timer-1
                if timer < 0:
                    print('Time is over!')
                    reset()
                time.sleep(1)

        if let == 'h':
            print('Starting timer!')
            timer = timer*3600
            while True:
                print(timer)
                timer = timer-1
                if timer < 0:
                    print('Time is over!')
                    reset()
                time.sleep(1)
main()