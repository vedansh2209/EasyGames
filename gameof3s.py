
def run():
    current = input("Type a number: ")
    current = float(current)
    while current != 1:
        if  current % 3 == 0:
            print ("%d 0" % current)
            current = current / 3
        elif ( current + 1 ) % 3 == 0:
            print ( "%d 1" % current )
            current = ( current + 1 ) / 3
        elif ( current - 1 ) % 3 == 0:
            print ("%d -1" % current)
            current = ( current - 1 ) / 3
    print (1)

def main():
    play = True
    while play:
        run()
        play = 'y' in input("Play Again? (y/n): ").lower()

if __name__ == '__main__':
    main()
