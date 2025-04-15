
print("Welcome to Mad Libs! Fill in the blanks to complete the story.\n")

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")

story = f"""
Once upon a time in a {adjective} {place}, there lived a {noun}.
Every day, it loved to {verb}. It was the happiest {noun} in all of {place}.
And they lived happily ever after.
"""


print("\nHere is your Mad Libs story:")
print(story)