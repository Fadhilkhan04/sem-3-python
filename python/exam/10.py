#ascii values to characters

uppercase_start = 65
lowercase_start = 97
uppercase_end = 90
lowercase_end = 122

print (f"Uppercase English ASCII values start from '{chr(uppercase_start)}' and end at '{chr(uppercase_end)}'.")
print (f"Lowercase English ASCII values start from '{chr(lowercase_start)}' and end at '{chr(lowercase_end)}'.")

def convert_to_alphabet( input_values):
    characters = []
    for value in input_values:
        try :
            num = int(value)
            if uppercase_start <= num <= uppercase_end or lowercase_start <= num <= lowercase_end :
                characters.append(chr(num))
            else:
                print(f"the number {num} is not valid ascii english alphabet skippinng")
        except ValueError:
            print(f"{value}is not valid ascii value")
    return characters
# main area

input_values = input("Enter ASCII values seperated by spaces:").split()
output = convert_to_alphabet(input_values)
if output :
    print (f"The converted characters are: {output}")
else :
    print ("No valid input provided.")
