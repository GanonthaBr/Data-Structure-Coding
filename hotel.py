"""
Hotel Booking System Requirements:
1. Room Management
   - Room types (Single, Double, Suite) with rates
   - Room availability by date
   - Room features (AC, TV, WiFi)

2. Booking Management
   - Make reservation (check-in/check-out dates)
   - Cancel reservation (with cancellation policy)
   - Modify reservation
   - Check room availability for dates

3. Billing
   - Calculate stay cost (room rate * nights)
   - Add extra charges (room service, minibar)
   - Apply taxes (12%)
   - Apply discounts for long stays

4. Reporting
   - Occupancy rate by date
   - Revenue report
   - Most booked room type
"""

class HotelBookingSystem:
    def __init__(self):
        self.rooms = {
            1: {
                'room_id':1, 'type':"single",'features':['wifi','water','electricity'],'price':1050.9, 'availability':True
            },
            2: {
                'room_id':2, 'type':"couple",'features':['wifi','water','electricity'],'price':1050.9, 'availability':True
            },
            3: {
                'room_id':3, 'type':"single",'features':['wifi','water','electricity'],'price':1050.9, 'availability':True
            }
        }
        self.bookings = {}
        self.customers = {}
        self.next_booking_id = 1
    
    # Room: {room_id, type, rate, features, availability}
    # Booking: {booking_id, customer_id, room_id, dates, status}
    # Implement: check_availability(), make_booking(), cancel_booking()
    # calculate_bill(), get_occupancy_report()

    def check_availability(self, room_id):
        avai = False
        for k, room in self.rooms.items():
            if room['room_id'] ==  room_id:
                if room['availability']:
                    avai =  True

                else:
                    avai =  False
            

        return avai
    def make_booking(self,room_id, customer_id, dates, status):
        available = self.check_availability(room_id)
        current_price = 0
        for k, room in self.rooms.items():
            if room['room_id'] == room_id:
                current_price = room['price']
                break

        if available:
            self.bookings[self.next_booking_id] = {
                'booking_id':self.next_booking_id,
                'customer_id': customer_id,
                'dates':dates,
                'status': 'Confirmed',
                'room_id': room_id,
                'price':current_price
            }
            self.next_booking_id += 1
        else:
            raise ValueError(f"The room with id {room_id} is not available")

    def cancel_booking(self, booking_id):
        for k,v in self.bookings.items():
            if k == booking_id:
                self.bookings[booking_id]['status'] = 'cancelled'

        return self.bookings

    def calculate_bill(self):
        total_bills = 0
        for k,bookings in self.bookings.items():
            if bookings['status'] ==  'Confirmed':
                total_bills += bookings['price']
        return total_bills

    def get_occupancy_report(self):
        pass



if __name__ == "__main__":
    hotel_system = HotelBookingSystem()
    print(hotel_system.check_availability(1))
    hotel_system.make_booking(1, 101, ['2024-10-01', '2024-10-05'], 'Confirmed')
    hotel_system.make_booking(2, 102, ['2024-10-02', '2024-10-06'], 'Confirmed')
    print(hotel_system.bookings)
    print(hotel_system.calculate_bill())
    hotel_system.cancel_booking(1)
    print(hotel_system.bookings)
    print(hotel_system.calculate_bill())