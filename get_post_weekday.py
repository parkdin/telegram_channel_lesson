from read_data import fromJson
def get_post_weekday(data:dict)->dict:
    """
    Return the number of posts for each weekday
    args:
        data: a dictionary of posts
    returns: a dictionary with the number of posts for each weekday
    """
    # Initialize a counter
    count = {}

    # Loop through the dictionary
    messages= data['messages']

    return count

# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_weekday(data)
print(count)

# Example:
# >>> get_post_weekday(data)

# Output:
# {
#     'monday': 10,
#     'tuesday': 14,
#     'wednesday': 7,
#     'thursday': 0,
#     'friday': 0,
#     'saturday': 0,
#     'sunday': 0
# }
