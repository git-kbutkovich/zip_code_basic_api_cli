import pandas as pd
from sqlalchemy import create_engine


p_db_name = "postgres"
p_user = "postgres"
p_pass = ""
port = '5433'

tab_file = "./zip_code_files/US.txt"

engine = create_engine(f"postgresql://{p_user}:{p_pass}@localhost:{port}/{p_db_name}")
df = pd.read_csv(tab_file)
df.to_sql("zip_codes", engine)
