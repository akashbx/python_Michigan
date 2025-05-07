def get_number(one_line):
    return int(one_line[:6])

def get_balance(one_line):
    return float(one_line[6:16])

def get_name(one_line):
    return one_line[16:].strip()

def equal_floats(x_flt, y_flt):
    return abs(x_flt - y_flt) < 1.0e-8

def main():
    prefix = input("Enter file name prefix: ")
    try:
        old_file = open(f"{prefix}.old.txt", "r")
        new_file = open(f"{prefix}.new.txt", "w")
    except IOError as e:
        print("File error:", e)
        return

    for line in old_file:
        if line.strip() == "999999":
            new_file.write("999999\n")
            break

        acct_num = get_number(line)
        balance = get_balance(line)
        name = get_name(line)

        print(f"Account: {acct_num} | Balance: {balance:.2f} | Name: {name}")

        while True:
            trans = input("Enter transaction (d=deposit, w=withdraw, c=close, a=advance): ").lower()

            if trans == 'd':
                try:
                    amt = float(input("Deposit amount: "))
                    if balance + amt > 9999999.99:
                        print("Deposit exceeds allowed maximum.")
                    else:
                        balance += amt
                except ValueError:
                    print("Invalid amount.")

            elif trans == 'w':
                try:
                    amt = float(input("Withdraw amount: "))
                    if balance - amt < 0:
                        print("Withdrawal exceeds available balance.")
                    else:
                        balance -= amt
                except ValueError:
                    print("Invalid amount.")

            elif trans == 'c':
                if equal_floats(balance, 0.0):
                    print("Account closed.")
                    break  # Do not write to new file
                else:
                    print("Cannot close account: balance not zero.")

            elif trans == 'a':
                new_file.write(f"{acct_num:06d}{balance:10.2f} {name}\n")
                break

            else:
                print("Invalid transaction code.")

    old_file.close()
    new_file.close()

if __name__ == "__main__":
    main()
