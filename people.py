from datetime import datetime
from flask import abort, make_response

def getTimeStamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": getTimeStamp(),
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": getTimeStamp(),
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": getTimeStamp(),
    }
}

def readAll():
    return list(PEOPLE.values())

def create(person):
    lname: str = person.get("lname")
    fname: str = person.get("fname")

    if (lname and lname not in PEOPLE):
        PEOPLE[lname] = {
            "fname": fname,
            "lname": lname,
            "timestamp": getTimeStamp(),
        }
    else:
        abort(
            406, f"Person with lastname {lname} already exists"
        )

    return PEOPLE[lname], 201

def readOne(lname: str):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )

def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = getTimeStamp()
        return PEOPLE[lname]
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )

def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )