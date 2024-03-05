import time

def wake_up(text = "Wake up", name = "Neo", n = 0.1):
    for i in range(len(text)):
        time.sleep(n)
        print("\033[1m\033[32m{}".format(text[i]), end ="")
    
    time.sleep(n)
    print(",", end = "")
    time.sleep(n)
    print(" ", end = "")

    time.sleep(n * 4)
    
    for i in range(len(name)):
        time.sleep(n)
        print(name[i], end = "")

    for i in range(3):
        time.sleep(n)
        print(".", end = "")
    
    print("\033[0m{}".format(" "))
    time.sleep(5)

    


wake_up()