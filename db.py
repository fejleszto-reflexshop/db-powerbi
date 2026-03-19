from postgrest import APIResponse
from supabase import create_client
import os
from dotenv import load_dotenv
import json

load_dotenv()

db_url = os.getenv('DATABASE_URL')
db_key = os.getenv('DATABASE_KEY')
db = create_client(db_url, db_key)

def get_orders_from_db():
    api_call: APIResponse = db.table('orders').select('*').execute()
    data = api_call.data

    return data

def write_orders_into_file():
    orders = get_orders_from_db()

    with open('orders.json', 'w') as outfile:
        json.dump(orders, outfile)