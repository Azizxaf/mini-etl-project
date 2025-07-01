from sqlalchemy import create_engine

def load_to_postgresql(df, table_name='customers'):
    # Update these settings with your actual PostgreSQL credentials
    db_user = 'your user'
    db_password = 'your password'
    db_host = 'localhost'
    db_port = '5432'
    db_name = 'etl_demo'

    # PostgreSQL connection string
    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    # Load DataFrame to PostgreSQL
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"✅ Loaded {len(df)} records into PostgreSQL table '{table_name}'")
