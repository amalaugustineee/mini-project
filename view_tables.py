import sqlite3

def view_tables():
    # Connect to the database
    conn = sqlite3.connect('instance/charity_chain.db')
    cursor = conn.cursor()
    
    # Get list of tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("\n=== Tables in Database ===\n")
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        print("-" * 50)
        
        # Get table schema
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        print("\nColumns:")
        for col in columns:
            print(f"- {col[1]} ({col[2]})")
        
        # Get table contents
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        print(f"\nContents ({len(rows)} rows):")
        for row in rows:
            print(row)
        print("\n")
    
    conn.close()

if __name__ == "__main__":
    view_tables() 