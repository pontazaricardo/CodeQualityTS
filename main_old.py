# " find . -type f -name '*.[ch]' -exec wc -l {} +"

import os
import re

# https://unix.stackexchange.com/questions/288409/counting-lines-of-code
# cat *.[ch] | wc -l
# find . -name '*.[ch]' -exec cat {} + | wc -l

# final: find . -type f -name '*.[ch]' -exec wc -l {} +
# folder_to_explore = f"~/tests_projects/06_SPHINCS-FIPS205-all-implementations/"

folder_to_explore = f"/home/liwuen/tests_projects/06_SPHINCS-FIPS205-all-implementations/"

string_to_execute = f"find {folder_to_explore} -type f -name '*.[ch]' -exec wc -l {{}} +"
command = os.popen(string_to_execute)
result_string = command.read()
# print(result_string)
lines = result_string.splitlines()


# folders_dict = {}
# with open('groups_to_search.txt') as f:
#     groups_search = f.read().splitlines()
#     for folders_to_search in groups_search:
#         results_by_commas = folders_to_search.split(',')
#         category = results_by_commas[0]
#         folder_in_category = results_by_commas[1]
#
#         folders_dict.update({folder_in_category: 0})





print(lines)
print(lines[0])
print(lines[1])

number_of_lines = re.search(r"([0-9]+)", lines[0]).group()

print(command.close())

