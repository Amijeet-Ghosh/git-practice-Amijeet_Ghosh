from datetime import datetime
from utils import add, subtract, multiply

def main():
    print("amijeet Ghosh")
    print(f"Today's Date: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"5 + 3 = {add(78, 45)}")
    print(f"10 - 4 = {subtract(17, 9)}")
    print(f"6 * 7 = {multiply(7, 13)}")

if __name__ == "__main__":
    main()