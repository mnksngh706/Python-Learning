str_1 = "James Bond is 007."
str_2 = "When the mo-*on hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

def words_counter(words):

    spaces_letters = ""
    word_count = 1

    for counted_words in words:
        if counted_words.isalnum() or counted_words.isspace() or counted_words == "-" or counted_words == "'":
            spaces_letters += counted_words

    for spaces_words in spaces_letters:
        if spaces_words == " ":
            word_count += 1

    return word_count


print(words_counter(str_1))
print(words_counter(str_2))
print(words_counter(str_3))