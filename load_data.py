import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:05251119@localhost/user"
)

df = pd.read_csv("cleaned_activities.csv")

df.rename(columns={
    'timestamp':'activity_time'
}, inplace=True)

df.to_sql(
    'activities',
    engine,
    if_exists='append',
    index=False
)

print("Жүктелді")