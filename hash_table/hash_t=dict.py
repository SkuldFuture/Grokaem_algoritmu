# GROCERY LIST
book = dict()

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

print(book)  # {'apple': 0.67, 'milk': 1.49, 'avocado': 1.49}
print(book["avocado"])  # 1.49

# REFERENCE BOOK
phone_book = {}

phone_book["jenny"] = 8675309
phone_book["emergency"] = 911

print(phone_book)  # {'jenny': 8675309, 'emergency': 911}
print(phone_book["jenny"])  # 8675309

# ELIMINATION OF DUPLICATES
voted = {}


def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")


print(check_voter("tom"))
print(check_voter("mike"))
print(check_voter("mike"))
