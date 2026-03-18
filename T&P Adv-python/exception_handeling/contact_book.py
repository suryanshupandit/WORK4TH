contacts = {"Alice": "1234567890"}

def add_contact(name, phone):
    try:
        if not name or not phone:
            raise ValueError("Fields cannot be empty.") 
        if name in contacts:
            raise Exception(f"Contact '{name}' already exists.") 
        if not (phone.isdigit() and len(phone) == 10):
            raise TypeError("Invalid phone format. Must be 10 digits.") 
        
        contacts[name] = phone
    except (ValueError, Exception, TypeError) as e:
        print(f"Save Error: {e}")

add_contact("Alice", "123") # Triggers duplicate and format errors