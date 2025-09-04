"""
==============================================
 Name        : Performing calculations
 Author      : Mostafa Elsoudy
 Instructions :
Add up and print the total number of course_completions.
--------------------------------
Print the largest value in course_completions.
--------------------------------
Add up the values in course_completions and then divide this by the number of elements to get the average.
--------------------------------
Round the average number of course completions to one decimal place.
==============================================
"""
# Print the total number of course completions
print(sum(course_completions))
--------------------------------
# Print the largest number of completions
print(max(course_completions))
--------------------------------
# Print the average number of completions
print(sum(course_completions) / len(course_completions))
--------------------------------
# Print the average number of completions, rounded to one decimal places
print(round(sum(course_completions) / len(course_completions), 1))
