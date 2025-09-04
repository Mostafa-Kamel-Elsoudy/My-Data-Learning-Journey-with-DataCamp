"""
==============================================
 Name        : Modifying string variables
 Author      : Mostafa Elsoudy
 Instructions :
Update the variable so that "Intro" now reads "Introduction".
Swap spaces to underscores throughout the string contained in most_popular_course.
Update most_popular_course so that it only contains lowercase characters.
==============================================
"""
most_popular_course = "Intro to Embeddings with the OpenAI API"

# Update the first word
most_popular_course = most_popular_course.replace("Intro", "Introduction")

print(most_popular_course)

most_popular_course = "Intro to Embeddings with the OpenAI API"

# Update the first word
most_popular_course = most_popular_course.replace("Intro", "Introduction")

# Swap spaces for underscores
most_popular_course = most_popular_course.replace(" ","_")

print(most_popular_course)

most_popular_course = "Intro to Embeddings with the OpenAI API"

# Update the first word
most_popular_course = most_popular_course.replace("Intro", "Introduction")

# Swap spaces for underscores
most_popular_course = most_popular_course.replace(" ", "_")

# Change to lowercase
most_popular_course = most_popular_course.lower()

print(most_popular_course)