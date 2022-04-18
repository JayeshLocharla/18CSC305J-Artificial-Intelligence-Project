from lib2to3.pgen2.tokenize import generate_tokens
from utilities.gen import generate_summary

def main():
    txt = input("Enter text file: ")
    generate_summary(txt)

if __name__ == '__main__':
    main()
