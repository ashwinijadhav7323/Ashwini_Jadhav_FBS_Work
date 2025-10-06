### Covert the time entered in hh , min and sec into seconds.

#Take a hours, minutes, seconds
hh = int(input("Enter Hours : "))
min = int(input("Enter Minutes : "))
sec = int(input("Enter Seconds : "))

#Perform operation
total_sec = (hh*3600) + (min*60) + sec 

#Display result
print(f'Total seconds are {total_sec}sec')
