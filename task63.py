test_data = [150, 25, 440]
for n in test_data:
    hours = (n // 60) % 24
    minutes = n % 60
    print(hours, minutes)