from read_data import fromJson


def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
    # Initialize a counter
    count = 0
    # Loop through the dictionary
    messages= data['messages']
    for i in messages:
        if i['type']=='message':          
            count+=int(i['date'][5:7])==month
        
  
 
    return count

# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_month(data,9)
print(count)