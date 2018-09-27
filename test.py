import time

x = "This is a Test2"

timeout = time.time() + 60 * 5

while True:
    if time.time() > timeout:   # Infinite loop will break after 5 minutes
        break
    else:
        print x