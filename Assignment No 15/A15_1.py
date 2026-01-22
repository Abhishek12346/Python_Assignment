

def main():
    Data=[10,23,42,45,32,65]
    result=lambda num: num * num
    Map=list(map(result,Data))
    print("  MAP a Data  =>",Map)

if __name__=="__main__":
    main()
