import datetime
import json
import operator


BIRTHDAYS = {
    "Toni": datetime.datetime(1991, 2, 11),
    "Josephine": datetime.datetime(1993, 11, 11),
    "Karla": datetime.datetime(1983, 12, 25),
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


def get_upcoming_birthdays(birthday_dict: dict) -> dict:
    today = datetime.date.today()

    tmp_birthdays = birthday_dict.copy()

    for name in tmp_birthdays:
        tmp_date = birthday_dict[name].date()
        tmp_date = datetime.date(today.year, tmp_date.month, tmp_date.day)
        if tmp_date < today:
            del birthday_dict[name]
        else:
            birthday_dict[name] = tmp_date
    return birthday_dict


if __name__ == '__main__':
    # write_birthdays_to_json(BIRTHDAYS, "birthdays.json")
    my_birthdays = read_birthdays_from_json("birthdays.json")
    upcoming_birthdays = get_upcoming_birthdays(my_birthdays)

    upcoming_birthdays = dict(sorted(upcoming_birthdays.items(),
                                     key=operator.itemgetter(1))
                              )

    for k,v in upcoming_birthdays.items():
        print(k, v)