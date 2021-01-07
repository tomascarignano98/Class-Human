from datetime import datetime
import time

dt = datetime.fromtimestamp(time.time())
dt1 = datetime.now()
dt2 = datetime.strptime("13/07/2021", "%d/%m/%Y")
print("dt:", dt)
print("dt1:", dt1)
print("dt2:", dt2.strftime("%Y/%m/%d"))
# strftime does jsut the opposite of strptime: it covnerts a dt object into a str
print(dt2 > dt1)
