bad_words = ("bad", "fake", "ugly")

comment = input("Enter Comment: ")

for word in bad_words:
    if word in comment.lower():
        comment = comment.lower().replace(word, "*" * len(word))

print("Filtered Comment:", comment)
