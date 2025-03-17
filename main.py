# " find . -type f -name '*.[ch]' -exec wc -l {} +"
import json
import os
import re

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
folder_to_explore_dictionary = {}
folder_label_dictionary = {}

filename = f'groups_to_search.json'
with open(filename) as file:
    data = json.load(file)
    for group in data["groups_to_search"]:
        category = group["category"]
        folder_to_explore = group["location"]
        folder_label = group["label"]

        if category not in category_dictionary:
            category_dictionary[category] = 0

        if folder_to_explore not in folder_to_explore_dictionary:
            folder_to_explore_dictionary[folder_to_explore] = 0

        if folder_to_explore not in folder_label_dictionary:
            folder_label_dictionary[folder_to_explore] = folder_label

        # At this point, we are located in a correct category - folder_to_explore pair. We check for the files
        code_lines_count_command = f"find {folder_to_explore} -type f -name '*.[c]' -exec wc -l {{}} +"
        counter_result = os.popen(code_lines_count_command)
        result_string = counter_result.read()

# print(lines)
# print(lines[0])
# print(lines[1])
#
# number_of_lines = re.search(r"([0-9]+)", lines[0]).group()
#
# print(command.close())

