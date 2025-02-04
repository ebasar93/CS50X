def main():
    time = input("What time is it?")
    time = convert(time)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 15:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    x,y = time.split(":")
    time = float(x) + float(y)/60
    return time

if __name__ == "__main__":
    main()

