def main():
    with open("dane/gra.txt") as dane:
        arr = [[y for y in x] for x in dane.read().strip().split("\n")]
    print(arr)

def zad1(arr):
    for i in range(len(arr)):

    
if __name__ == '__main__':
    main()
