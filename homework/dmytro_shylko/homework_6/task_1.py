# pylint: disable=trailing-whitespace
text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel.\
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

words = text.split()
new_text = []

for word in words:
    if "," in word:
        word = word.replace(",", "ing,")
        new_text.append(word)
    elif "." in word:
        word = word.replace(".", "ing.")
        new_text.append(word)
    else:
        word += "ing"
        new_text.append(word)

print(" ".join(new_text))
