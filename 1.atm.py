import math
import datetime
def convert_to_two_digits(number_str):
    if len(number_str) != 4:
        raise ValueError("Input must be a 4-digit number.")
    
    first_two_digits = int(number_str[:2])
    last_two_digits = int(number_str[2:])
    
    return first_two_digits, last_two_digits
z=[]

def convert_to_single_digit(number):
    number_str = str(number)
    modified_number_str = ""
    i=0
    for digit in number_str:
        if digit == '0':
            z.append(0)            
            modified_number_str += '1'
        else:
            z.append(1)
            modified_number_str += digit
        i=i+1
    modified_number = str(modified_number_str)
    print(modified_number)
    return modified_number

four_digit_number_str = str(input("Enter the Pin"))
result=convert_to_single_digit(four_digit_number_str)
first, second = convert_to_two_digits(result)

def split_two_digit_number(number):
    # Extract the tens digit
    tens_digit = number // 10

    # Extract the ones digit
    ones_digit = number % 10

    return tens_digit, ones_digit
n=2

number = []
total=[]


# Initialize an empty array to store the numbers
number.append(first)
number.append(second)

for i in range(n):
    tens_digit, ones_digit = split_two_digit_number(number[i])
    total.append(tens_digit+ones_digit)


def change_last_bit_to_complement(decimal_number):
    # Find binary representation of the number
    binary_number = list(bin(decimal_number)[2:].zfill(3))

    # Complement the last three bits
    for i in range(1, 4):
        if i==1:
            binary_number[-i] = '1' if binary_number[-i] == '0' else '0'

    
    decimal_output = int(''.join(binary_number), 2)

    return decimal_output
def flip_last_before_rightmost_1(decimal_number):
    binary_number = list(bin(decimal_number)[2:].zfill(3))
    for i in range(1, 4):
        if i==2:
            binary_number[-i] = '1' if binary_number[-i] == '0' else '0'
    decimal_output = int(''.join(binary_number), 2)
    return decimal_output
def flip_last_before_rightmost_2(decimal_number):
    binary_number = list(bin(decimal_number)[2:].zfill(3))
    for i in range(1, 4):
        if i==3:
            binary_number[-i] = '1' if binary_number[-i] == '0' else '0'
    decimal_output = int(''.join(binary_number), 2)

    return decimal_output
def flip_last_and_before_rightmost_1(decimal_number):
    binary_number = list(bin(decimal_number)[2:].zfill(3))
    for i in range(1, 4):
        if i==2 or i==1:
            binary_number[-i] = '1' if binary_number[-i] == '0' else '0'
    decimal_output = int(''.join(binary_number), 2)
    return decimal_output
def flip_last_and_before_rightmost_2(decimal_number):
    binary_number = list(bin(decimal_number)[2:].zfill(3))
    for i in range(1, 4):
        if i==3 or i==1:
            binary_number[-i] = '1' if binary_number[-i] == '0' else '0'
    decimal_output = int(''.join(binary_number), 2)
    return decimal_output
def flip_before_rightmost_2_and_before_rightmost_1(decimal_number):
    binary_number = list(bin(decimal_number)[2:].zfill(3))
    for i in range(1, 4):
        if i==2 or i==3:
            binary_number[-i] = '1' if binary_number[-i] == '0' else '0'
    decimal_output = int(''.join(binary_number), 2)

    return decimal_output
def flip_last_three_bits(decimal_number):
    binary_number = list(bin(decimal_number)[2:].zfill(3))
    for i in range(1, 4):
        binary_number[-i] = '1' if binary_number[-i] == '0' else '0'
    decimal_output = int(''.join(binary_number), 2)
    return decimal_output

flipped_decimal_number=[]
type=[]
def case0():
    t= change_last_bit_to_complement(total[i])
    flipped_decimal_number.append(number[i]+t)            
def case1():
    t= flip_last_before_rightmost_1(total[i])
    flipped_decimal_number.append(number[i]+t)  
def case2():
    t= flip_last_before_rightmost_2(total[i])
    flipped_decimal_number.append(number[i]+t)      
def case3():
    t= flip_last_and_before_rightmost_1(total[i])
    flipped_decimal_number.append(number[i]+t)  
def case4():
    t= flip_last_and_before_rightmost_2(total[i])
    flipped_decimal_number.append(number[i]+t)  
def case5():
    t= flip_before_rightmost_2_and_before_rightmost_1(total[i])
    flipped_decimal_number.append(number[i]+t)  
   
cases = {
    0: case0,
    1: case1,
    2: case2,
    3: case3,
    4: case4,
    5: case5
   
}

def reduce_to_single_digit_and_divide_by_2(number):
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    result = number / 2
    result =math.ceil(result)
    return result

for i in range(n):
   current_time = datetime.datetime.now()
   s=current_time.second
   output = reduce_to_single_digit_and_divide_by_2(s)
   cases.get(output)()
    
deviation=[]
ad=0
ad=float(ad)
for i in range(n):
    t=flipped_decimal_number[i]-number[i]
    deviation.append(t)  

max=-999
min=999

for i in range(n):
    if(abs(deviation[i])>max):
        max=abs(deviation[i])  
    if(abs(deviation[i])<min):
        min=abs(deviation[i])
    ad=abs(deviation[i])+ad     
    
ad=ad/n

def join_to_four_digits(first, second):
    if not (isinstance(first, int) and isinstance(second, int)):
        raise ValueError("Input must be integers.")
    if not (0 <= first <= 99 ):
        first=number[1]-deviation[1]
        deviation[1]=-deviation[1]
       
    if not(0 <= second <= 99 ):
        second=number[0]-deviation[0]
        deviation[0]=-deviation[0]
    return int(str(first).zfill(2) + str(second).zfill(2))
first_two_digits = flipped_decimal_number[0]
last_two_digits = flipped_decimal_number[1]
four_digit_number = join_to_four_digits(last_two_digits,first_two_digits)
binary_representation = bin(four_digit_number)[2:]

def split_binary_into_two_digits(binary):
    if len(binary) > 14:
        raise ValueError("Input binary number must be 14 digits or less.")    
    padded_binary = binary.zfill(14)
    digits_array = [padded_binary[i:i+2] for i in range(0, len(padded_binary), 2)]
    return digits_array
digits_array = split_binary_into_two_digits(binary_representation)
gene=[]
for i in range(7):
    if(digits_array[i]=='00'):
        gene.append("T")
    elif(digits_array[i]=='01'):
        gene.append("G")
    elif(digits_array[i]=='10'):
        gene.append("C")
    elif(digits_array[i]=='11'):
        gene.append("A")

def array_to_string(array):
    return "".join(array)
encrypted = array_to_string(gene)
with open(r'C:\Users\hp5cd\OneDrive\Desktop\Research paper\Dna\1.deviation.txt', 'w') as file:
    for element in deviation:
        file.write(str(element) + ',')
with open(r'C:\Users\hp5cd\OneDrive\Desktop\Research paper\Dna\2.Encrypted.txt', 'w') as file:
    file.write(str(encrypted) + '\t')
with open(r'C:\Users\hp5cd\OneDrive\Desktop\Research paper\Dna\3.number.txt', 'w') as file:
    for element in z:
        file.write(str(element) + ',')
print("Encrypted:", encrypted)

