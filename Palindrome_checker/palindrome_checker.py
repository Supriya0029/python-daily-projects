text = input("enter a word:")

cleaned = ""
for char in text:
    if char.isalnum():
        cleaned += char.lower()

if cleaned == cleaned[::-1]:
    print("Palindrome!")
else:
    print("not a palindrome.")
