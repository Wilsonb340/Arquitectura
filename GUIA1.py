from os import name


def main():
    number = input("Ingresa el número: ")
    from_base = int(input("Ingresa la base actual (2, 8, 10, 16): "))
    name = number

    if is_valid_base(from_base):
        print("Número en bases:")
        print("Hexadecimal:", convert_base(number, from_base, 16))
        print("Octal:", convert_base(number, from_base, 8))
        print("Binario:", convert_base(number, from_base, 2))
        print("Decimal:", convert_base(number, from_base, 10))
    else:
        print("Base no válida")

def convert_base(number, from_base, to_base):
    decimal_number = int(number, from_base)
    return format(decimal_number, f'0{to_base}b')

def is_valid_base(base):
    return base == 2 or base == 8 or base == 10 or base == 16

if name == "_main_":
    main()
