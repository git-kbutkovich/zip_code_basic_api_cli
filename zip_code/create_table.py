import psycopg2




def create_tables():
    """create tables in PostgreSQL locally"""

    commands = """
        DROP TABLE IF EXISTS public.zip_codes;
        CREATE TABLE public.zip_codes (
            country_code VARCHAR(3) NOT NULL,
            zip_code VARCHAR(10) NOT NULL,
            city VARCHAR(255),
            admin_region VARCHAR(25),
            admin_region_code VARCHAR(5),
            admin_subregion VARCHAR(25),
            admin_subregion_code VARCHAR(5),
            dmin_subregion_2 VARCHAR(25),
            admin_subregion_code_2 VARCHAR(5),
            latitude decimal NOT NULL,
            longitude decimal NOT NULL,
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW()
        )
        """
    return commands


def execute_postgres():

    conn = None
    p_db_name = "postgres"
    p_user = "postgres"
    p_pass = ""
    port = '5433'
    query = "select count(1) from zip_codes;"
    try:
        print("Attempting to connect")
        conn = psycopg2.connect(database=p_db_name, user=p_user, password=p_pass, host="localhost", port=port)

        cur = conn.cursor()

        # cur.execute(create_tables())
        # print("table created")
        cur.execute(query)
        answer = cur.fetchone()
        print("answer fetched")
        print(answer)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print("db_connection closed")


if __name__ == "__main__":
    execute_postgres()
