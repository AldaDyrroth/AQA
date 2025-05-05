def format_phone_number(digits):
    if digits.isdigit() == True:
        formatted_num = '(' + digits[0:3] + ') ' + digits[3:6] + '-' + digits[6:10]
    return (formatted_num)

print(format_phone_number('9234348983'))