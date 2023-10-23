import re

string = "a"
# pattern = re.compile("luiz\.")
pattern = re.compile("^a")

# x = re.fullmatch(pattern, string) # "luiz."
x = re.fullmatch(pattern, string) # "luiz."
# x = re.search(pattern, string)
# x = re.findall(pattern, string) # ee luiz ed luiz."

print(x)
