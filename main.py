# " find . -type f -name '*.[ch]' -exec wc -l {} +"
import json
import os
import re

import numpy as np
import matplotlib.pyplot as plt

#from main_old import folder_to_explore

# https://unix.stackexchange.com/questions/288409/counting-lines-of-code
# cat *.[ch] | wc -l
# find . -name '*.[ch]' -exec cat {} + | wc -l

# final: find . -type f -name '*.[ch]' -exec wc -l {} +
# folder_to_explore = f"~/tests_projects/06_SPHINCS-FIPS205-all-implementations/"

# folder_to_explore = f"/home/liwuen/tests_projects/06_SPHINCS-FIPS205-all-implementations/"
#
# string_to_execute = f"find {folder_to_explore} -type f -name '*.[ch]' -exec wc -l {{}} +"
# command = os.popen(string_to_execute)
# result_string = command.read()
# # print(result_string)
# lines = result_string.splitlines()


category_dictionary = {}
folder_label_dictionary = {}

category_totals = {}
label_totals = {}

filename = f'groups_to_search.json'
with open(filename) as file:
    data = json.load(file)
    for group in data["groups_to_search"]:
        category = group["category"]
        folder_to_explore = group["location"]
        folder_label = group["label"]

        if folder_to_explore not in folder_label_dictionary:
            folder_label_dictionary[folder_to_explore] = folder_label

        if category not in category_dictionary:
            category_dictionary[category] = {}
            category_totals[category] = 0

        if folder_to_explore not in category_dictionary[category]:
            category_dictionary[category].update({folder_to_explore: 0})

        if folder_label not in label_totals:
            label_totals[folder_label] = 0

# At this point, we are located in a correct category - folder_to_explore pair. We check for the files

for category in category_dictionary:
    for folder in category_dictionary[category]:
        # The variable 'folder' is the folder we need to search.
        # Searching in the nested cycle  guarantees that we keep proper counting

        code_lines_count_command = f"find {folder} -type f -name '*.[c]' -exec wc -l {{}} +"
        counter_result = os.popen(code_lines_count_command)
        result_string = counter_result.read()

        if result_string == "":
            print(f'[{category}][{folder}]: Not file with ending [.c] was found, or any possible [.c] file might be empty.\n')
        else:
            #At least one file was found. We count
            total_number_of_detected_lines = 0
            list_of_subfolders = result_string.splitlines()

            for line in list_of_subfolders[0:len(list_of_subfolders) - 1]: # We iterate until the next-to-last one, as the last one contains TOTAL by default.
                number_of_detected_code_lines_str = re.search(r"([0-9]+)", line).group()
                number_of_detected_code_lines = int(number_of_detected_code_lines_str)
                total_number_of_detected_lines = total_number_of_detected_lines + number_of_detected_code_lines

                # Adding to the final dictionaries
                category_totals[category] = category_totals[category] + number_of_detected_code_lines
                label_totals[folder_label_dictionary[folder]] = label_totals[folder_label_dictionary[folder]] + number_of_detected_code_lines

                print(line)

            # We check for consistency
            total_outputed_in_command = int(re.search(r"([0-9]+)", list_of_subfolders[len(list_of_subfolders)-1]).group())
            category_dictionary[category][folder] = category_dictionary[category][folder] + total_number_of_detected_lines

            print(f'[{category}][{folder}]: Calculated total = {total_number_of_detected_lines}')
            print(f'[{category}][{folder}]: Reported total = {category_dictionary[category][folder]}\n')
            if total_outputed_in_command != category_dictionary[category][folder]:
                print(f'Inconsistency found in [{category}][{folder}]: Calculated total = {category_dictionary[category][folder]} vs. Reported total = {total_outputed_in_command}\n')


print("Final report: \n")
#At this point, we already searched everywhere
for category in category_dictionary:
    for folder in category_dictionary[category]:
        print(f'[{category}][{folder}]: {category_dictionary[category][folder]}')

for category in category_totals:
    print(f'[{category}]: Total = {category_totals[category]}')

for folder_label in label_totals:
    print(f'[{folder_label}]: Total = {label_totals[folder_label]}')


# Print figures
# Figure 1: Size by category

plot_by_category = plt.figure(1)

barWidth = 0.5

categories_to_print = [key for key, value in category_totals.items()]
values_to_print = [value for key, value in category_totals.items()]

plt.title('Total number of code lines per category')
plt.xlabel('Lines of code')
plt.ylabel('Categories')
plt.bar(categories_to_print, values_to_print, barWidth)

plot_by_category.show()



plot_by_label = plt.figure(2)

barWidth = 0.5

categories_to_print = [key for key, value in label_totals.items()]
values_to_print = [value for key, value in label_totals.items()]

plt.title('Total number of code lines per label')
plt.xlabel('Lines of code')
plt.ylabel('Label')
plt.bar(categories_to_print, values_to_print, barWidth)

plot_by_label.show()
input()
#
#
#
#
#
#
# barWidth = 0.25
# fig = plt.subplots(figsize =(12, 8))
#
# IT = [12, 30, 1, 8, 22]
# ECE = [28, 6, 16, 5, 10]
# CSE = [29, 3, 24, 25, 17]
#
# br1 = np.arange(len(IT))
# br2 = [x + barWidth for x in br1]
# br3 = [x + barWidth for x in br2]
#
# plt.bar(br1, IT, color ='r', width = barWidth,
#         edgecolor ='grey', label ='IT')
# plt.bar(br2, ECE, color ='g', width = barWidth,
#         edgecolor ='grey', label ='ECE')
# plt.bar(br3, CSE, color ='b', width = barWidth,
#         edgecolor ='grey', label ='CSE')
#
# plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
# plt.ylabel('Students passed', fontweight ='bold', fontsize = 15)
# plt.xticks([r + barWidth for r in range(len(IT))],
#         ['2015', '2016', '2017', '2018', '2019'])
#
# plt.legend()
# plt.show()

# counter_result = os.popen(code_lines_count_command)
# result_string = counter_result.read()
#
# if result_string == "":
#     print ('null')
# else:
#     print('not null')

# print(lines)
# print(lines[0])
# print(lines[1])
#
# number_of_lines = re.search(r"([0-9]+)", lines[0]).group()
#
# print(command.close())

