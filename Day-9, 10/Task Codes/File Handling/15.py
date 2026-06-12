# 15. Store employee records in a binary file and search by EmpID.
import pickle
records = [{"EmpID": 101, "Name": "Alice"}, {"EmpID": 102, "Name": "Bob"}]
f = open("emp.dat", "wb")
pickle.dump(records, f)
f.close()

f = open("emp.dat", "rb")
data = pickle.load(f)
search_id = int(input("Enter EmpID to search: "))
for emp in data:
    if emp["EmpID"] == search_id:
        print("Record found:", emp)
f.close()\n