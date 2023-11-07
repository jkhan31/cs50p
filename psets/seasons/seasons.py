from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    try:
        dob = date.fromisoformat(input("Date of Birth: "))
    except:
        sys.exit("Invalid date")

    age_in_minutes = age_to_minutes(dob)
    print(minutes_to_words(age_in_minutes))


def age_to_minutes(birth_date):
    today = date.today()
    age = today - birth_date
    age_in_minutes = age.total_seconds() / 60
    return int(age_in_minutes)

def minutes_to_words(minutes):
   words = p.number_to_words(minutes, andword="")
   return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()