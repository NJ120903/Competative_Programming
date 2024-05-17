def parse_time(time_str):
    hh, mm = map(int, time_str.split(':'))
    return hh * 60 + mm

def format_time(minutes):
    if minutes < 60:
        return f"{minutes} minutes"
    else:
        hours = minutes // 60
        minutes %= 60
        if minutes == 0:
            return f"{hours} hours"
        else:
            return f"{hours} hours and {minutes} minutes"

day = 1
while True:
    try:
        s = int(input().strip())
        appointments = []
        for _ in range(s):
            start_time, end_time, *description = input().split()
            start_minutes = parse_time(start_time)
            end_minutes = parse_time(end_time)
            appointments.append((start_minutes, end_minutes))

        appointments.sort()  # Sort appointments by start time

        longest_nap_start = 0
        longest_nap_duration = 0
        for i in range(1, len(appointments)):
            nap_start = appointments[i-1][1]
            nap_end = appointments[i][0]
            nap_duration = nap_end - nap_start
            if nap_duration > longest_nap_duration:
                longest_nap_duration = nap_duration
                longest_nap_start = nap_start

        # Check if there is a nap opportunity after the last appointment
        last_end_time = appointments[-1][1]
        if last_end_time < 18 * 60:  # Assuming the last appointment ends before 18:00
            nap_duration = 18 * 60 - last_end_time
            if nap_duration > longest_nap_duration:
                longest_nap_duration = nap_duration
                longest_nap_start = last_end_time

        nap_start_hh, nap_start_mm = divmod(longest_nap_start, 60)
        print(f"Day #{day}: the longest nap starts at {nap_start_hh:02d}:{nap_start_mm:02d} and will last for {format_time(longest_nap_duration)}.")
        day += 1
    except EOFError:
        break
