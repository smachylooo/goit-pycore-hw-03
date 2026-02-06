from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int] | str:
    try:
        min, max, quantity = int(min) , int(max), int(quantity)
    except ValueError:
        return 'Should be 3 numbers'
    
    if quantity <= 0:
        return "Quantity must be positive"
    
    if quantity > (max - min + 1):
        return 'Quantity is too big'
    
    if min < 1 or max <= min:
        return "Invalid range"

    return sorted(list(sample(range(min, max + 1), quantity)))
