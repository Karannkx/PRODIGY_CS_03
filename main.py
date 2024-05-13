import re

def check_password_complexity(password):
    length_pattern = r'.{8,}'  
    uppercase_pattern = r'[A-Z]'
    lowercase_pattern = r'[a-z]'
    digit_pattern = r'\d'
    special_char_pattern = r'[!@#$%^&*()-+=]'

    length_check = bool(re.match(length_pattern, password))
    uppercase_check = bool(re.search(uppercase_pattern, password))
    lowercase_check = bool(re.search(lowercase_pattern, password))
    digit_check = bool(re.search(digit_pattern, password))
    special_char_check = bool(re.search(special_char_pattern, password))

    score = sum([length_check, uppercase_check, lowercase_check, digit_check, special_char_check])

    if score == 5:
        return "Password is very strong"
    elif score >= 3:
        return "Password is strong"
    elif score >= 2:
        return "Password is moderate"
    else:
        return "Password is weak"

def main():
    password = input("Enter your password: ")
    complexity_feedback = check_password_complexity(password)
    print(complexity_feedback)

if __name__ == "__main__":
    main()
