import time
def lap_timer():
    start_time = time.time()
    last_time = start_time
    lap = 1
    print("press enter key")
    try:
        while True:
            input()
            lap = round((time.time() - last_time), 2)
            total = round((time.time() - start_time), 2)
            print("Lap ", lap)
            print("Total Time: ", total)
            print("Lap Time: ", lap)
            last_time = time.time()
            lap += 1
    except:
        print("exit")
if __name__ == "__main__":
    lap_timer()