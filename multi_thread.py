import threading

def hello(name):
    print('The child thread, ID: {}'.format(threading.get_ident()))
    print('Hello ' + name)

def main():
    print('The main thread, ID: {}'.format(threading.get_ident()))
    print('----------------------------------------')

    t = threading.Thread(target=hello, args=('Earth', ))

    t.start()
    t.join()

    print('----------------------------------------')
    print('The main thread, ID: {}'.format(threading.get_ident()))

if __name__ == '__main__':
    main()
