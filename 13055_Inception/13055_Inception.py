
def main():
    lines = []
    dream_state = []

    count = int(input().strip())
    for i in range(count):
        line = input().strip()
        if "Sleep" in line:
            dream_state.append(line.split(" ")[1])
        if "Kick" == line and dream_state:
            dream_state.pop()
        if "Test" == line and dream_state:
            print(dream_state[-1])
        elif "Test" == line and not dream_state:
            print("Not in a dream")


if __name__ == '__main__':
    main()
