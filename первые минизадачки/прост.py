import random

data = [
    {"bookingid": 1},
    {"bookingid": 2},
    {"bookingid": 3},
    {"bookingid": 4}
]

print(random.choice(data)["bookingid"])