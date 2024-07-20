import pandas as pd

# Load the CSV file
file_path = 'C:/Users/kanig/Downloads/Bengaluru_House_Data.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print("Initial Data:")
print(data.head())

# Example filters:
# Filter by specific area_type
area_type_filter = 'Super built-up  Area'
filtered_data = data[data['area_type'] == area_type_filter]

# Filter by location
location_filter = 'Electronic City Phase II'
filtered_data = filtered_data[filtered_data['location'] == location_filter]

# Filter by size
size_filter = '2 BHK'
filtered_data = filtered_data[filtered_data['size'] == size_filter]

# Filter by price range (e.g., price less than 50)
price_max = 50.0
filtered_data = filtered_data[filtered_data['price'] < price_max]

# Display the filtered data
print("\nFiltered Data:")
print(filtered_data)
