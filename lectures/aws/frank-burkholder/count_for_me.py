# use this program to demonstrate the utility of screen on AWS
import time

if __name__=='__main__':
    i = 1
    while True:
        print("The count is {0}.".format(i))
        time.sleep(1)
        i += 1

    
