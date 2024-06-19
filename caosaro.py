
def nadjiNajveciBroj(broj1, broj2):
    if(broj1>broj2):
        return broj1
    else:
        return broj2

def main():
    broj1 = input("Unesite prvi broj")
    broj2 = input("Unesite drugi broj")
    veciBroj= nadjiNajveciBroj(broj1, broj2)
    print(veciBroj)

main()


