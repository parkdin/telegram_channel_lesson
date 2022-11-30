from read_data import fromJson
def get_post_per_month(data:dict)->dict:
  
    
    return count


# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_per_month(data)
print(count)