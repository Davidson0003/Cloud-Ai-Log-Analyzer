def group_by_time(parsed_logs):
    time_map = {}

    for log in parsed_logs:
        time = log["timestamp"]
        time_map.setdefault(time, 0)
        time_map[time] += 1

    return time_map
