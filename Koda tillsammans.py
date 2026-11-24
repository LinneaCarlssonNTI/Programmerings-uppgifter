def visa_meny():
    print("Vad vill du göra?")
    print("[1] sätta in pengar")
    print("[2] ta ut pengar")
    print("[3] visa saldo")
    print("[4] avsluta")

def sätta_in(saldo, belopp):
    saldo += belopp
    return saldo

def ta_ut(saldo, belopp):
    if saldo >= belopp:
        saldo -= belopp
        print(f"Tar ut {belopp} kr.")
        return saldo
    else:
        print("Det finns inte tillräckligt med pengar. Du är PANK!")
        return saldo

def visa_saldo(saldo):
    print(saldo)

saldo = 1000

while True:
    visa_meny()
    val = input()

    if val == "1":
        belopp = int(input("Hur mycket vill du sätta in?"))
        saldo = sätta_in(saldo, belopp)
    
    elif val == "2":
        belopp = int(input("Hur mycket vill du ta ut?"))
        saldo = ta_ut(saldo, belopp)
    
    elif val == "3":
        visa_saldo(saldo)

    else:
        break

