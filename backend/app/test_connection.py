from database.connection import engine

try:
    with engine.connect() as connection:
        print("✅ Connected to PostgreSQL successfully!")
except Exception as e:
    print(f"❌ Connection failed: {e}")