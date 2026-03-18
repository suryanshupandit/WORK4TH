class InventoryError(Exception): "Base class for inventory" 

class OutOfStockError(InventoryError): "Raised when stock is 0" 
class InvalidProductIDError(InventoryError): "Raised for bad IDs" 

def check_stock(pid):
    if pid < 0:
        raise InvalidProductIDError("IDs must be positive.") 

try:
    check_stock(-1)
except InventoryError as e:
    print(f"Custom Framework Caught: {e}")