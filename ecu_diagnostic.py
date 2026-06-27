#ECU DIAGNOSTIC LOG ANALYZER V2
import random
import time

fault_database = [{"code": "P0010",
               "description":"Camshaft position actuator circuit",
               "severity":"medium"},
               
              {"code":"P0115",
                "description": "Engine coolant temperature sensor circuit",
                "severity":"medium"},
                
              {"code":"P0171",
               "description":"system too lean",
               "severity":"high"},
                 
              {"code":"P0300",
               "description":"random misfire detected",
               "severity":"high"},
                  
              {"code":"P0420",
               "description":"catalyst system efficiency below thershold",
               "severity":"medium"},
               
               {"code":"P0500",
                "description":"vehicle speed sensor malfuntion",
                "severity":"low"},
                
                {"code":"P0700",
                "description":"transmission control system malfunction",
                "severity":"high"},
                
                {"code":"P0128",
                "description": "coolant temperture emission system large leak",
                "severity":"low"},
                
                {"code":"P0455",
                "description":"evaporative emission system large leak",
                "severity":"medium"},
                
                {"code":"P0562",
                "description":"system voltage low",
                "severity": "high"}]

vehicles = [
    {  "vehicle name": "Bolero",
        "vehicle type": "SUV",
        "fuel type": "Diesel"},

    {   "vehicle name": "Pagani",
        "vehicle type": "hypercar",
        "fuel type": "Petrol" }]

fault_logs = [{"vehicle name":"Bolero",
            "code":"P0300",
            "description":"random misfire detected",
            "severity":"high"},

            {"vehicle name":"Bolero",
            "code":"P0420",
            "description":"catalyst system efficiency below thershold",
            "severity":"medium"},

            {"vehicle name":"Pagani",
            "code":"P0700",
            "description":"transmission control system malfunction",
            "severity":"high"},
            
            {"vehicle name":"Lamborgini",
            "code":"P0300",
            "description":"random misfire detected",
            "severity":"high"}]

fault_count = {}
severity_order = {"high": 1, "medium": 2, "low": 3}

def add_fault_logs():
    vehicle = input("Enter the name of the vehicle:- ")
    code = input("Enter the fault code:- ")
    description = input("Enter the description of fault code:- ")
    severity = input("Enter the severity level:- ")
    fault_logs.append({"vehicle name": vehicle, "code": code, "description": description, "severity": severity})

def add_fault_code():
    fault_code = input("Enter the fault code:- ")
    description = input("Enter the description of fault code:- ")
    severity = input("Enter the severity level:- ")
    fault_database.append({"fault code": fault_code, "description": description, "severity": severity})
    print("Your fault code is successfully added with below details!")
    print(f"Fault code:- {fault_code}")
    print(f"Description of code:- {description}")
    print(f"Severity level:- {severity}")
    with open("fault logs.txt","a") as file:
        file.write(f"{fault_code},{description},{severity}\n")
    return

def show_all_fault():
    for all in fault_database:
        print(f"Fault code:- {all['code']}")
        print(f"Description of fault code:- {all['description']}\n")
    return

def search_fault_code():
    fault_code = input("Enter the fault code you want to search:- ")
    for code in fault_database:
        if code["code"].lower().strip() == fault_code.lower().strip():
            print(f"Fault code founded successfully!")
            print(f"Fault code:- {fault_code}")
            print(f"Description of fault code:- {code['description']}")
            print(f"Severity level of fault code:- {code['severity']}")
            return
    else:
        print("The code you have enter is not available in ECU Diagonist. Please add fault code first!")
        add_fault_code()

def delete_fault_code():
    fault_code = input("Enter the fault code which you want to delete:- ")
    for code in fault_database:
        if code["code"].lower().strip() == fault_code.lower().strip():
            print(f"Your fault {fault_code} is deleted successfully!")
            fault_database.remove(code)
            return
    else:
        print("You have invaild fault code. Please try again later!")

def count_fault_code():
    count = 0
    for fault in fault_database:
        count+= 1
    print(f"Total fault code are {count}")
    if not fault_database:
        print("NO Fault code available. Plesae try again later!")
        return

def show_highseverity_fc():
    for severity in fault_database:
        if severity["severity"].lower().strip() == "high".lower().strip():
            print(f"High severity fault code are:- {severity['code']}")
            print(f"Description of High severity code is:- {severity['description']}\n")
    else:
        print("No fault code founded. Please try again later!")
    return

def show_mediumseverity_fc():
    for severity in fault_database:
        if severity["severity"].lower().strip() == "medium".lower().strip():
            print(f"High severity fault code are:- {severity['code']}")
            print(f"Description of High severity code is:- {severity['description']}\n")
    else:
        print("No fault code founded. Please try again later!")
    return

def show_lowseverity_fc():
    for severity in fault_database:
        if severity["severity"].lower().strip() == "low".lower().strip():
            print(f"High severity fault code are:- {severity['code']}")
            print(f"Description of High severity code is:- {severity['description']}\n")
    else:
        print("No fault code founded. Please try again later!")
    return

def most_common_fc():
    if not fault_logs:
        print("No fault logs available.")
        return
    fault_count = {}
    for fault in fault_logs:
        code = fault["code"]
        if code in fault_count:
            fault_count[code] += 1
        else:
            fault_count[code] = 1
    most_common_code = ""
    highest_count = 0
    for code in fault_count:
        if fault_count[code] > highest_count:
            highest_count = fault_count[code]
            most_common_code = code
    for fault in fault_logs:
        if fault["code"] == most_common_code:
            print("========== MOST COMMON FAULT ==========")
            print(f"Fault Code : {fault['code']}")
            print(f"Description : {fault['description']}")
            print(f"Severity : {fault['severity']}")
            print(f"Occurrences : {highest_count}")
            return

def fault_statistics():
    count = 0
    high = 0
    medium = 0
    low = 0
    vehicle_health = ""
    vehicle_name = input("Enter the vehicle name of which you want to do fault statistics check:- ")
    for vehicle in fault_logs:
        if vehicle["vehicle name"].lower().strip() == vehicle_name.lower().strip():
            count += 1
            if vehicle["severity"] == "high":
                high += 1
            if vehicle["severity"] == "medium":
                medium += 1
            if vehicle["severity"] == "low":
                low += 1
            if high == 0:
                vehicle_health = "Healthy"
            elif high <= 2:
                vehicle_health = "Needs Inspection"
            else:
                vehicle_health = "Critical"
            fault_count = {}
            code = vehicle["code"]
            if code in fault_count:
                fault_count[code] += 1
            else:
                fault_count[code] = 1
                highest = 0
                most_common = ""
            for code in fault_count:
                if fault_count[code] > highest:
                    highest = fault_count[code]
                    most_common = code  
    else:
        print("The you enter is invailde. Please try again later!")     
    print("========== FAULT STATISTICS ==========")
    print(f" Vehicle : {vehicle_name}")
    print(f" Total Faults : {count}")
    print(f" High severity : {high}")
    print(f" Medium severity : {medium}")
    print(f" Low severity : {low}")
    print(f" Most Common Fault : {most_common}")
    print(f" Occurrences : {highest}")
    print(f" Vehicle Health : {vehicle_health}")
    return

def save_faultlogs_tofile():
    with open("fault logs.txt","a") as file:
        for fault in fault_logs:
            file.write(f"{fault['vehicle name']},{fault['code']},{fault['description']},{fault['severity']}\n")
        print("Fault logs savaed successfully!")
    return

def load_faultlogs_fromfile():
    fault_logs.clear()
    with open("fault logs.txt","r") as file:
        for line in file:
            data = line.strip().split(",")
            fault_logs.append({"vehicle name": data[0], "code": data[1], "description": data[2], "severity": data[3]})
            print(data)
    print("Fault logs loaded successfully!")
    return

def clear_all_fc():
    vehicle_name = input("Enter the vehicle name of which you want to clear fault:- ")
    choice = input("1. Do you want to remove fault from vehicle you enter or 2. Do you want to remove all fault:- ")
    for code in fault_logs[:]:
        if code["vehicle name"].lower().strip() == vehicle_name.lower().strip():
            if choice == "2":
                fault_logs.clear()
            print("You have successfully cleared all fault codes!")
        elif choice == "1":
            fault_logs.remove(code)
        print(f"Your fault code is successfully remove from your vehicle : {vehicle_name}")
    return
            
def update_fault_information():
    fault_code = input("Enter the fault code which you want to update:- ")
    description = input("Enter the updated description:- ")
    severity = input("Enter the updated severity level:- ")
    for update in fault_database:
        if update["code"].lower().strip() == fault_code.lower().strip():
            update["description"] = description
            update["severity"] = severity
    else:
        print("You have enter invalid fault code. Please try again later!")
    print("========== UPDATEED INFORMATION ==========")
    print(f" Fault code : {update['code']}")
    print(f" Description : {update['description']}")
    print(f" Severity : {update['severity']}")
    return

def sort_fcby_severity():
    severity_order = {"high": 1, "medium": 2, "low": 3}
    sorted(fault_logs, key=lambda x: severity_order[x["severity"]])
    sorted_faults = [{"vehicle name": "Bolero", "code": "P0300", "severity": "High"},
                    {"vehicle name": "Bolero", "code": "P0420", "severity": "Medium"},
                    {"vehicle name": "Pagani", "code": "P0500", "severity": "Low"}]
    print("========== SORTED FAULTS ==========")
    for fault in sorted_faults:
        print(fault["vehicle name"])
        print(fault["code"])
        print(fault["severity"])
        print("\n")
    return

def export_diagnostic_report():
    count = 0
    high = 0
    medium = 0
    low = 0
    vehicle_name = input("Enter vehicle name:- ")
    with open("diagnostic_report.txt", "w") as file:
        file.write("========== ECU DIAGNOSTIC REPORT ==========\n")
        file.write(f"Vehicle : {vehicle_name}\n")
        file.write("Fault Details\n")
        for fault in fault_logs:
            if fault["vehicle name"].lower().strip() == vehicle_name.lower().strip():
                count += 1
                file.write(f"Code : {fault['code']}\n")
                file.write(f"Description : {fault['description']}\n")
                file.write(f"Severity : {fault['severity']}\n")
                if fault["severity"].lower() == "high":
                    high += 1
                elif fault["severity"].lower() == "medium":
                    medium += 1
                elif fault["severity"].lower() == "low":
                    low += 1
        if high == 0:
            vehicle_health = "Healthy"
        elif high <= 2:
            vehicle_health = "Needs Inspection"
        else:
            vehicle_health = "Critical"
        file.write("--------------------------------------\n")
        file.write(f"Total Faults : {count}\n")
        file.write(f"High Severity : {high}\n")
        file.write(f"Medium Severity : {medium}\n")
        file.write(f"Low Severity : {low}\n")
        file.write(f"Vehicle Health : {vehicle_health}\n")
        file.write("Generated By : ECU Diagnostic Log Analyzer V2\n")
        file.write("Developer : Krish Singatkar\n")
    print("Diagnostic Report Exported Successfully!")

def scan_demo_ecu():
    count = 0
    vehicle_health = ""
    selected_vehicle = random.choice(vehicles)
    vehicle_name = selected_vehicle["vehicle name"]
    print("========== ECU DEMO SCAN ==========")
    print("Connecting to ECU...")
    time.sleep(2)
    print("Reading Fault Codes...")
    time.sleep(2)
    print("\nScan Complete!\n")
    print(f"Vehicle : {vehicle_name}\n")
    for fault in fault_logs:
        if fault["vehicle name"].lower().strip() == vehicle_name.lower().strip():
            count += 1
            print(f"Fault Code : {fault['code']}")
            print(f"Description : {fault['description']}")
            print(f"Severity : {fault['severity']}\n")
    if count == 0:
        vehicle_health = "Healthy"
    elif count <= 2:
        vehicle_health = "Needs Inspection"
    else:
        vehicle_health = "Critical"
    print(f"Total Faults : {count}")
    print(f"Vehicle Health : {vehicle_health}")

while True:
    print("======== ECU DIAGNOIST ========")
    print("1. Add Fault code.")
    print("2. Show all fault codes.")
    print("3. Search fault code.")
    print("4. Delete fault code.")
    print("5. Count total faults.")
    print("6. Show high severity faults.")
    print("7. Show medium severity fault.")
    print("8. Show low sverity faults.")
    print("9. Most common fault code.")
    print("10. Fault statistics.")
    print("11. Save Fault logs to file.")
    print("12. Load fault logs form file.")
    print("13. Clear all fault logs.")
    print("14. Update fault information.")
    print("15. Sort Faults by severity.")
    print("16. Export diagnostic report.")
    print("17. Scan demo Ecu.")
    print("18. Exit.")

    choice = input("Enter what you want to do:- ")
    if choice == "1":
        add_fault_code()
    elif choice == "2":
        show_all_fault()
    elif choice == "3":
        search_fault_code()
    elif choice == "4":
        delete_fault_code()
    elif choice == "5":
        count_fault_code()
    elif choice == "6":
        show_highseverity_fc()
    elif choice == "7":
        show_mediumseverity_fc()
    elif choice == "8":
        show_lowseverity_fc()
    elif choice == "9":
        most_common_fc()
    elif choice == "10":
        fault_statistics()
    elif choice == "11":
        save_faultlogs_tofile()
    elif choice == "12":
        load_faultlogs_fromfile()
    elif choice == "13":
        clear_all_fc()
    elif choice == "14":
        update_fault_information()
    elif choice == "15":
        sort_fcby_severity()
    elif choice == "16":
        export_diagnostic_report()
    elif choice == "17":
        scan_demo_ecu()
    elif choice == "18":
        print("Thankyou for using your ECU DIAGNOSTIC. Please visit again!")
        break
