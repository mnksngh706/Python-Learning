the_string = "North America"
print(the_string.rjust(17))
print(the_string.ljust(17, "*"))

center_plus = the_string.center(16, "+")
print(center_plus)
print(the_string.lstrip())
print(center_plus.rstrip(), "+")
print(center_plus.lstrip(), "+")
print(the_string.replace("North", "South"))