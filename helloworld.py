import sys

def main():
    print("Hellow World! From Python: " + str(sys.version_info))
    if sys.version_info >= (3,6) and sys.version_info < (3, 7):
        #lets's make this script fall for Python 3.6
        raise Exception('Python version 3.6.x is unsupported!')
        
if __name__ == "__main__":
    main()
