from read_data import fromJson

def get_post_per_week(data:dict,month:int)->dict:
    """
    Return the number of posts for each week of a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        dict: a dictionary with the number of posts for each week.
    """
    # Initialize a counter
    count = {}
    # Loop through the dictionary
    messages= data['messages']
    for week in range(1, 6):
        count[week] = 0
        for msg in messages:
            if msg['type']=='message':          
                count[week]+=int(msg['date'][5:7])==month and (week*7-7 < int(msg['date'][8:10]) <= week*7)

    return count

# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_per_week(data,11)
print(count)

# Example:
# >>> get_post_per_week(data,9)
# {1: 0, 2: 0, 3: 0, 4: 0}


