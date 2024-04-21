import random
import pandas as pd
import numpy as np

# List of random Tunisian first names and last names
tunisian_first_names = ["Ahmed", "Mohamed", "Fatma", "Houda", "Sami", "Nadia", "Ali", "Hatem", "Amira", "Lamia","Youssef", "Ines", "Salma", "Walid", "Rania", "Karim", "Wafa", "Mehdi", "Amina", "Chiraz"]
tunisian_last_names = ["Ben Salah", "Mzoughi", "Chaabane", "Sassi", "Gharbi", "Khaldi", "Hachicha", "Bouazizi", "Rekik", "Jouini","Ayari", "Karray", "Mejri", "Baccar", "Bouzid", "Saadi", "Ferchichi", "Gabsi", "Mansouri", "Ben Hassen"]

# Function to generate a random Tunisian phone number
def generate_phone_number():
    prefix = random.choice(['2', '5', '9'])  # Choose landline or mobile prefix
    number = ''.join([random.choice('0123456789') for _ in range(7)])  # Generate 7 random digits
    return f"{prefix}{number}"

# Function to generate random longitude and latitude around a center point
def generate_random_address(center_latitude, center_longitude, radius_km):
    # Generate random distance (in km) and angle (in radians)
    u = np.random.uniform(0, 1)  # Random number between 0 and 1
    v = np.random.uniform(0, 1)  # Random number between 0 and 1
    radius_in_degrees = radius_km / 111.32  # Approximate km to degrees conversion
    w = radius_in_degrees * np.sqrt(u)
    t = 2 * np.pi * v
    # Calculate coordinates offsets
    delta_latitude = w * np.cos(t)
    delta_longitude = w * np.sin(t)
    # Calculate new coordinates
    new_latitude = center_latitude + delta_latitude
    new_longitude = center_longitude + delta_longitude
    return new_latitude, new_longitude

# Generate data for the table
num_records = 30  # Number of records in the table
center_latitude = 36.944897
center_longitude = 10.175510
radius_km = 5.0  # Radius within which to generate random addresses

data = []
for _ in range(num_records):
    first_name = random.choice(tunisian_first_names)
    last_name = random.choice(tunisian_last_names)
    email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"
    phone_number = generate_phone_number()
    satisfaction_level = random.choice(["bien", "très bien", "neutre", "mauvais", "très mauvais"])
    latitude, longitude = generate_random_address(center_latitude, center_longitude, radius_km)

    data.append([first_name, last_name, email, phone_number, satisfaction_level, longitude, latitude])

# Create a DataFrame
columns = ['First Name', 'Last Name', 'Email Address', 'Phone Number', 'Satisfaction Level', 'Longitude', 'Latitude']
df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(df)
