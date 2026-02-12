
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London"
}

# Adding an item
country_capitals["Italy"] = "Rome"
print("After adding Italy:", country_capitals)

print(country_capitals.values()) 

print(country_capitals.keys()) 

print("\nIterating through the dictionary:")
for country, capital in country_capitals.items():
    print(f"{country}: {capital}")

# Removing an item using pop()
capital = country_capitals.pop("Canada")
print("After popping Canada (removed capital):", capital)
print("Current dictionary:", country_capitals)

# Clearing the dictionary
country_capitals.clear()
print("After clearing the dictionary:", country_capitals)

# Re-creating the dictionary for demonstration of methods
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London"
}

# Using get() method
print("Capital of England:", country_capitals.get("England"))
print("Capital of France (not in dict):", country_capitals.get("France"))

# Using items() method
print("Key-Value pairs:", list(country_capitals.items()))

# Using update() method
new_capitals = {"Italy": "Rome", "France": "Paris"}
country_capitals.update(new_capitals)
print("After updating with new capitals:", country_capitals)

# keys = ['a', 'b', 'c']
# default_value = 0
# my_dict = {key: default_value for key in keys}
# print(my_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}
