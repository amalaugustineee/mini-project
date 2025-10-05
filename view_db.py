import sqlite3
import pandas as pd

def view_database():
    # Connect to the database
    conn = sqlite3.connect('instance/charity_chain.db')
    
    # Get all tables
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("\n=== Database Contents ===\n")
    
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        print("-" * 80)
        
        # Read table into pandas DataFrame
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        
        # Set display options to show all columns
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        
        print(df.to_string())
        print("\n")

if __name__ == "__main__":
    view_database() 