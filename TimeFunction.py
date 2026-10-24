def convert_time(total_minutes):
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60 
    return hours, remaining_minutes

hours, remaining_minutes = convert_time(130)

print("Hours:", hours)
print("Remaining minutes:", remaining_minutes)
