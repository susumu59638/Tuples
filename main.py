# Creating a Tuple
countries = ("Japan", "England", "India", "Ireland", "Benin", "Cuba")
print(countries)

# Packing a Tuple
name = ("I", "am", "Susumu")
for item in name:
    print(item,end = " ")

# Unpacking in Tuples
family = ("Susumu","Akira","Ayumi","Satoshi","Toshiko","Ogiwa","Hiroko","Michiya")
son,daughter,mother,father,grandmother,grandfather,grandmother2,grandfather2 = family
print()
print(f"My name is {son}")
print(f"My sister's name is {daughter}")
print(f"My mother's name is {mother}")
print(f"My father's name is {father}")
print(f"My mother's mother's name is {grandmother}")
print(f"My mother's father's name is {grandfather}")
print(f"My father's mother's name is {grandmother2}")
print(f"My father's father's name is {grandfather2}")