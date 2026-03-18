inventory = {"Laptop": 0}
valid_coupons = ["SAVE10"]

def place_order(item, coupon):
    try:
        if inventory.get(item) == 0:
            raise Exception(f"Item {item} is out of stock.")
        if coupon not in valid_coupons:
            raise ValueError("Invalid coupon code.") 
    except Exception as e:
        print(f"Order Failed: {e}")

place_order("Laptop", "FAKE50")