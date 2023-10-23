# A common use case of generators is to work with data streams or large files, like CSV files.

# Example 1
# def infinity_number_gen():
#     num = 0
#     while True:
#         yield num
#         num += 1
#
#
# for n in infinity_number_gen():
#     print(n, end=', ')

# Example 2
file_name = "techcrunch.csv"
# Reading each line from the file with a generator expression.
lines = (line for line in open(file_name))

# Using another generator expression in concert with the previous one to split each line (DATA) into a list.
list_line = (s.rstrip().split(",") for s in lines)

# The keys are the column names cols from line 4.
# The values are the rows in list form, created in line 3.

# Pulling the column names out of techcrunch.csv.
# Since the column names tend to make up the first line in a CSV file, you can grab that with a short next() call
cols = next(list_line)

# creating dictionaries and unites them with a zip()
company_dicts = (dict(zip(cols, data)) for data in list_line)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)

total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")
