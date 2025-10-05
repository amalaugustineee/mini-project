import sqlite3
from tabulate import tabulate

def run_query(query):
    try:
        # Connect to the database
        conn = sqlite3.connect('instance/charity_chain.db')
        cursor = conn.cursor()
        
        # Execute the query
        cursor.execute(query)
        
        # Fetch results
        rows = cursor.fetchall()
        
        if not rows:
            print("\nNo results found.")
            return
        
        # Get column names
        columns = [description[0] for description in cursor.description]
        
        # Print results in a nice table format
        print("\nResults:")
        print(tabulate(rows, headers=columns, tablefmt="grid"))
        print(f"\nTotal rows: {len(rows)}")
            
    except sqlite3.Error as e:
        print(f"\nDatabase Error: {e}")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        conn.close()

def main():
    print("\n=== SQLite Database Query Tool ===")
    print("\nAvailable tables: charity, user")
    print("\nExample queries:")
    print("1. SELECT * FROM charity")
    print("2. SELECT name, email FROM charity")
    print("3. SELECT * FROM user")
    print("4. SELECT name, email FROM charity WHERE admin_approved = 1")
    
    while True:
        print("\nEnter your SQL query (or 'exit' to quit):")
        query = input().strip()
        
        if query.lower() == 'exit':
            break
            
        if query:
            run_query(query)

if __name__ == "__main__":
    main() 