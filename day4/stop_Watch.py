import time

timer_limit = int(input("Please enter the limit "))
for second in range(1, timer_limit + 1):
    print(timer_limit + 1 - second, ' ', ' left')
    time.sleep(1)
