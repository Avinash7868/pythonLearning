name = "Avinash"
print(name.startswith("avi"))
print(name.startswith("Avi"))
print(name.endswith("ash"))


# F strings (in Python) / Template litrals (in JS)
print(f"Good Morning {name}")


# Problem 1 Make String Dynamic
letter = '''Dear <|Name|>, 
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>","Avinash").replace("<|Date|>" , "22nd Feb 2025"))
