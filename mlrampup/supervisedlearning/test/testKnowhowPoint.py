
def test():
    a = 0
    return

def main():
    i = 1
    test.a = 1
    test()
    print(str(locals()))
    print(str(globals()))

print(test.a)

if __name__ == '__main__':
    main()
