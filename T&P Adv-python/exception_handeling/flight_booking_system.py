def book_flight(passenger_name, seat_available):
    try:
        if not passenger_name:
            raise ValueError("Invalid passenger details.") 
        if not seat_available:
            raise RuntimeError("Seat no longer available.") 
            
        print(f"Ticket confirmed for {passenger_name}!")
    except (ValueError, RuntimeError) as e:
        print(f"Booking Error: {e}")

book_flight("", False)