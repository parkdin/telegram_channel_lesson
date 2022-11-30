from read_data import fromJson
def get_post_per_week(data:dict,month:int)->dict:
    """
    Return the number of posts for each week of a given month
    args:
        data: a dictionary of posts
        month: as number between 1 and 12
    returns: a dictionary with the number of posts for each week
    """
    # Initialize a counter
    count = {}
    # Loop through the dictionary
    messages= data['messages']

    return 

# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_per_week(data,9)
print(count)

# Example:
# >>> get_post_per_week(data,9)
# {1: 0, 2: 0, 3: 0, 4: 0}


