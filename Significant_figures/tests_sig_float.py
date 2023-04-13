from sig_float import sig_float

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

print("Sig fig count tests:" + GREEN)
num = sig_float("00122.9800")
print(f"1) 00122.9800 -> {num.sig_figs()}")

num = sig_float("12000")
print(f"2) 12000 -> {num.sig_figs()}")

num = sig_float("12000.")
print(f"3) 12000. -> {num.sig_figs()}")

num = sig_float("0012000.")
print(f"4) 0012000. -> {num.sig_figs()}")

num = sig_float("2536.000")
print(f"5) 2536.000 -> {num.sig_figs()}")

num = sig_float("1.000")
print(f"6) 1.000 -> {num.sig_figs()}")

num = sig_float("0.00033")
print(f"7) 0.00033 -> {num.sig_figs()}")

num = sig_float("12.09")
print(f"8) 12.09 -> {num.sig_figs()}")

num = sig_float("000001")
print(f"9) 000001 -> {num.sig_figs()}")

num = sig_float("10.")
print(f"10) 10. -> {num.sig_figs()}")


print(RESET + "\nAddition and subtraction tests:" + GREEN)
num1 = sig_float("13.0198")
num2 = sig_float("1.2")
print(f"1) {num1} + {num2} = {num1 + num2}")

num1 = sig_float("94")
num2 = sig_float("15")
num3 = sig_float("182.113")
print(f"2) {num1} + {num2} + {num3} = {num1 + num2 + num3}")

num1 = sig_float("59.21")
num2 = sig_float("18.8722")
print(f"3) {num1} - {num2} = {num1 - num2}")

num1 = sig_float("8.679")
num2 = sig_float("0.3")
num3 = sig_float("5.88")
print(f"4) {num1} + {num2} + {num3} = {num1 + num2 + num3}")

num1 = sig_float("2.36")
num2 = sig_float("5.4")
print(f"5) {num1} + {num2} = {num1 + num2}")

num1 = sig_float("7.2361")
num2 = sig_float("8.42")
print(f"6) {num1} + {num2} = {num1 + num2}")

num1 = sig_float("420.")
num2 = sig_float("3.51")
print(f"7) {num1} + {num2} = {num1 + num2}")

# Should be 500
num1 = sig_float("500")
num2 = sig_float("1.365")
print(RED + f"8) {num1} + {num2} = {num1 + num2}")

print(RESET)