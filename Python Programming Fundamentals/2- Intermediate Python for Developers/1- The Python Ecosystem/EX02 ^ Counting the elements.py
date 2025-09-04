"""
==============================================
 Name        : Counting the elements
 Author      : Mostafa Elsoudy
 Instructions :
Use a function to count the number of key-value pairs in course_ratings,
storing as a variable called num_courses, then print the variable.
----------------------------------------------
Use a function to count the number of courses in course_completions, 
storing as num_courses, and print this variable.
----------------------------------------------
Use a function to count the number of characters in most_popular_course, storing as title_length, and print the variable.
==============================================
"""
course_ratings = {"LLM Concepts": 4.7, 
                  "Introduction to Data Pipelines": 4.75, 
                  "AI Ethics": 4.62, 
                  "Introduction to dbt": 4.81}

# Print the number of key-value pairs
num_courses = len(course_ratings)
print(num_courses)
----------------------------------------------
course_completions = [97, 83, 121, 205, 56, 174, 92, 117, 164]

# Find the number of courses
num_courses = len(course_completions)
print(num_courses)
-----------------------------------------------
most_popular_course = "Introduction to dbt"

# How many characters are in most_popular_course?
title_length = len(most_popular_course)
print(title_length)
