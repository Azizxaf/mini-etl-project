from etl import extract_fake_data, transform_data, load_to_postgresql

if __name__ == "__main__":
    df_extracted = extract_fake_data(10)
    print("📦 Extracted Data:")
    print(df_extracted)

    df_transformed = transform_data(df_extracted)
    print("\n🔧 Transformed Data:")
    print(df_transformed)

    load_to_postgresql(df_transformed)
