import datetime
import json

BIRTHDAYS = {
    "Mama": datetime.datetime(1965, 1, 23),
    "Anna": datetime.datetime(1988, 5, 22),
    "Kati": datetime.datetime(1986, 12, 2),
}

def write_birthdays_to_json(birthdays: dict, filename: str):

    tmp_dict = {}
    for name, birthdate in birthdays.items():
        print(name, birthdate)
        tmp_dict[name] = birthdate.isoformat()

    with open(filename, "w") as f:
        json.dump(tmp_dict, f)

def read_birthdays_from_json(filename: str) -> dict:
    with open(filename, "r") as f:
        content = json.load(f)

    for name in content:
        content[name] = datetime.datetime.fromisoformat(content[name])

    return content


if __name__ == '__main__':
    print(BIRTHDAYS)
    write_birthdays_to_json(BIRTHDAYS, "birthdays.json")
    my_birthdays = read_birthdays_from_json("birthdays.json")

    today = datetime.date.today() # heutiges Datum

    tmp_birthdate = my_birthdays.copy()

    for name in tmp_birthdate:
        tmp_date = my_birthdays[name].date()
        tmp_date = datetime.date(today.year, tmp_date.month, tmp_date.day)
        tmp_date.year = today.year
        if tmp_date < today:
            del my_birthdays[name]
    print(my_birthdays)