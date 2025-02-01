import os
from dotenv import load_dotenv

load_dotenv()

host_stage = os.getenv("URL_STAGE")
pol_url = os.getenv("POL_PROD_URL")
mol_url = os.getenv("MOL_PROD_URL")