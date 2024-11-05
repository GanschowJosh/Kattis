def convert_to_24_hour_format(time_str):
    time, period = time_str.split()
    hour, minute = map(int, time.split(':'))
    
    if period == 'a.m.':
        if hour == 12:  # 12 a.m. is 00:00 in 24-hour format
            hour = 0
    else:  # p.m.
        if hour != 12:  # 12 p.m. remains 12:xx in 24-hour format
            hour += 12
    
    return f"{hour:02}:{minute:02}", time_str  

def sort_appointments(test_cases):
    results = []
    for appointments in test_cases:
        converted_times = [convert_to_24_hour_format(time) for time in appointments]
        
        converted_times.sort()
        sorted_times = [original for _, original in converted_times]
        
        results.append(sorted_times)
    
    return results

def process_input_and_output():
    test_cases = []
    while True:
        n = int(input())
        if n == 0:
            break
        appointments = [input().strip() for _ in range(n)]
        test_cases.append(appointments)
    
    sorted_days = sort_appointments(test_cases)
    
    for i, day in enumerate(sorted_days):
        if i > 0:
            print()  # Print blank line between test cases
        for appointment in day:
            print(appointment)

process_input_and_output()
