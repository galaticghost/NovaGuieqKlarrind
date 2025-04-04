i = 0
dpto = 0
while i < 105:
    dpto += 1
    name = "XIDGJDIJDJI"
    with open("test.txt","a") as file:
        file.write(f"INSERT INTO employees_nopk(employeeid,employeename,dptoid) VALUES ({dpto},'{name}',{dpto});\n")
    i += 1