student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56,76,98]
}



import pandas

students_data_frame = pandas.DataFrame(student_dict)
print(students_data_frame)

#Looping through dictionaries
#for (key, value) in student_dict.items():
    # print(value)

# Loop through rows of a dataframe

for (index, row) in students_data_frame.iterrows():
    # print(row)
    pass

{new_key:new_value for (index, row) in df.iterrows()}

testt