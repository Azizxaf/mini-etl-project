from faker import Faker
import pandas as pd

fake = Faker()

def extract_fake_data(n=10):
    data = []
    for _ in range(n):
        customer = {
            'name': fake.name(),
            'email': fake.email(),
            'address': fake.address(),
            'phone_number': fake.phone_number(),
            'birthdate': fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat()
        }
        data.append(customer)
    return pd.DataFrame(data)
