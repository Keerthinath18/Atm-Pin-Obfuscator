with open(r'C:\Users\hp5cd\OneDrive\Desktop\Research paper\Dna\2.Encrypted.txt', 'r') as file:
    key = file.read()
number=[]
with open(r'C:\Users\hp5cd\OneDrive\Desktop\Research paper\Dna\1.deviation.txt', 'r') as file:
    number = file.read().split(',')
    number = number[:-1]
    number = [int(element) for element in number]
key = key.replace('\t', '')
digits_array = [char for char in key]
gene=[]
for i in range(7):
    if(digits_array[i]=='T'):
        gene.append("00")
    elif(digits_array[i]=='G'):
        gene.append("01")
    elif(digits_array[i]=='C'):
        gene.append("10")
    elif(digits_array[i]=='A'):
        gene.append("11")

result = str(int("".join(gene)))
result= int(result, 2)

def convert_to_two_digits(number):
    number_str = str(number)
    if len(number_str) not in [3, 4]:
        raise ValueError("Input must be a 3 or 4-digit number.")
    if (len(number_str)==3):
        number_str = str("{:04d}".format(number))
    first_two_digits = str(number_str[:2])
    last_two_digits = str(number_str[2:])

    return (first_two_digits, last_two_digits)
first, second = convert_to_two_digits(result)
first=int(first)
second=int(second)
first=first-number[1]
second=second-number[0]


def convert_to_four_digit(first, second):
    if not (isinstance(first, int) and isinstance(second, int)):
        raise ValueError("Input must be integers.")
    if not (0 <= first <= 99 and 0 <= second <= 99):
        raise ValueError("Input integers must be between 0 and 99.")
    four_digit_number = (str(first).zfill(2) + str(second).zfill(2))
    return four_digit_number
four_digit_number = convert_to_four_digit(second,first)
(single_digit_sequence) = [int for int in four_digit_number]
z=[]
with open(r'C:\Users\hp5cd\OneDrive\Desktop\Research paper\Dna\3.number.txt', 'r') as file:
    z = file.read().split(',')
    z = z[:-1]
    z= [int(element) for element in z]
for i in range(4):
    if(z[i]==0):
        single_digit_sequence[i]=  '0'
result_string = "".join(str(digit) for digit in single_digit_sequence)
print("decrypted value:",result_string)
