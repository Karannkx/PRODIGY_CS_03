```
# Password Complexity Checker

This Python script checks the complexity of a password based on various criteria such as length, presence of uppercase and lowercase letters, digits, and special characters.

## Usage

1. Run the script in a Python environment.
2. Enter the password you want to check.
3. The script will provide feedback on the complexity of the password.

## Criteria

- **Length**: Minimum length of 8 characters.
- **Uppercase Letters**: At least one uppercase letter.
- **Lowercase Letters**: At least one lowercase letter.
- **Digits**: At least one digit.
- **Special Characters**: At least one special character from the set [!@#$%^&*()-+=].

## Feedback

- **Very Strong**: Password meets all criteria.
- **Strong**: Password meets at least three criteria.
- **Moderate**: Password meets at least two criteria.
- **Weak**: Password meets fewer than two criteria.

## Example

```python
Enter your password: MyP@ssw0rd
Password is very strong
```

```python
Enter your password: pass
Password is weak
```
