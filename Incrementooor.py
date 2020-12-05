import os

a = "LogMeUp.txt"

def main():
    if a in os.listdir():
        f = open(a, "r");
        new_number = int(f.read()) + 1; f.close()
        f = open(a, "w");
        f.write(str(new_number));
        f.close();
    else: 
        f = open(a, "w");
        f.write(str(1));
    
if __name__ == "__main__":
    xx = 1;
    print(xx)
    main();


