def add(firstname: str, lastname:str | None):
    return firstname + " " + (lastname or " ")

firstname = "shahrukh"
lastname = "khan"

name = add(firstname, lastname)
print(name)


