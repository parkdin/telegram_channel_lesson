from read_data import fromJson


def get_posts_peer_day(data:dict)->dict:
    """
    Return the number of posts for each month

    Args:
        data (dict): a dictionary of posts

    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    # Initialize a counter
    count = {}  
    # Loop through the dictionary
    
    messages= data['messages']
    for month in range(1, 13):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            count[month] = {}
            for day in range(1, 32):
                count[month][day] = 0
                for msg in messages:
                    if msg['type']=='message':          
                        count[month][day]+=int(msg['date'][5:7])==month and int(msg['date'][8:10])==day
        elif month in [4, 6, 9, 11]:
            count[month] = {}
            for day in range(1, 31):
                count[month][day] = 0
                for msg in messages:
                    if msg['type']=='message':          
                        count[month][day]+=int(msg['date'][5:7])==month and int(msg['date'][8:10])==day
        elif month == 2 and int(msg['date'][:4]) % 4 == 0:
            count[month] = {}
            for day in range(1, 30):
                count[month][day] = 0
                for msg in messages:
                    if msg['type']=='message':          
                        count[month][day]+=int(msg['date'][5:7])==month and int(msg['date'][8:10])==day
        elif month == 2 and int(msg['date'][:4]) % 4 != 0:
            count[month] = {}
            for day in range(1, 30):
                count[month][day] = 0
                for msg in messages:
                    if msg['type']=='message':          
                        count[month][day]+=int(msg['date'][5:7])==month and int(msg['date'][8:10])==day
    
    return count

# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_posts_peer_day(data)
print(count)