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

    return api_call.data


def flatten_dict(d, parent_key='', sep='_'):
    items = []

    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k

        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, f"{new_key}_{i}", sep=sep).items())
                else:
                    items.append((f"{new_key}_{i}", item))

        else:
            items.append((new_key, v))

    return dict(items)


def write_orders_into_file():
    orders = get_orders_from_db()

    flattened_orders = []

    for order in orders:
        items = order.get("Items", {}).get("Item", [])

        # normalize single item → list
        if isinstance(items, dict):
            items = [items]
        elif not isinstance(items, list):
            items = []

        order_data = {k: v for k, v in order.items() if k not in ["Items", "id"]}

        flat_order = flatten_dict(order_data)

        if not items:
            flattened_orders.append(flat_order)
            continue

        for item in items:
            if not isinstance(item, dict):
                continue

            flat_item = flatten_dict(item)

            new_entry = flat_order.copy()

            for k, v in flat_item.items():
                new_entry[f"item_{k}"] = v

            flattened_orders.append(new_entry)

    with open('orders.json', 'w', encoding='utf-8') as outfile:
        json.dump(flattened_orders, outfile, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    write_orders_into_file()