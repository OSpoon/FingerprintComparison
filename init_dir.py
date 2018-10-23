import os

if __name__ == '__main__':
    if not os.path.exists(os.getcwd()+'/all/dist'):
        os.makedirs('all/dist')
    if not os.path.exists(os.getcwd() + '/diff'):
        os.makedirs('diff')
    if not os.path.exists(os.getcwd() + '/old'):
        os.makedirs('old')
