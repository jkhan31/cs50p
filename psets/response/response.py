from validator_collection import validators, checkers, errors

def main():
    print(email_validation(input("What's your email address? ")))

def email_validation(s):
    if checkers.is_email(s) == False:
        return "Invalid"
    else:
        return "Valid"

if __name__ == "__main__":
    main()