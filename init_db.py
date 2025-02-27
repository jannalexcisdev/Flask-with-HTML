import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="my_practice",
        user="postgres",
        password="@dmin098"
    )

def initialize_db():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute('DROP TABLE IF EXISTS users;')

            cur.execute('''
                CREATE TABLE users (
                    id SERIAL PRIMARY KEY,
                    firstName VARCHAR(255) NOT NULL,
                    lastName VARCHAR(255) NOT NULL,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL
                );
            ''')

            cur.executemany('''
                INSERT INTO users (firstName, lastName, username, email, password) 
                VALUES (%s, %s, %s, %s, %s)
            ''', [
                ('John', 'Doe', 'johndoe', 'john@example.com', 'hashed_password1'),
                ('Jane', 'Smith', 'janesmith', 'jane@example.com', 'hashed_password2'),
                ('Alice', 'Johnson', 'alicej', 'alice@example.com', 'hashed_password3')
            ])

            conn.commit()
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    initialize_db()  # Run only when executed directly
