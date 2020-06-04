#rates
day_shift = 27.1000
night_shift = 30.3500
overtime1 = 37.9400
overtime2 = 48.7800
##########################
travel = 20.00
meal = 14.78
##########################
print("==================SUNDAY=======================")
sunday2 = float(input("Enter overtiime 2.0 hours: "))
print("===============================================")
print()
print("==================MONDAY=======================")
monday = float(input("Enter normal day shift hours: "))
monday_n = float(input("Enter normal night shift hours: "))
monday1 = float(input("Enter overtiime 1.5 hours: "))
monday2 = float(input("Enter overtiime 2.0 hours: "))
print("===============================================")
print()
print("==================TUESDAY=======================")
tuesday = float(input("Enter normal day shift hours: "))
tuesday_n = float(input("Enter normal night shift hours: "))
tuesday1 = float(input("Enter overtiime 1.5 hours: "))
tuesday2 = float(input("Enter overtiime 2.0 hours: "))
print("===============================================")
print()
print("==================WEDNESDAY=======================")
wednesday = float(input("Enter normal day shift hours: "))
wednesday_n = float(input("Enter normal night shift hours: "))
wednesday1 = float(input("Enter overtiime 1.5 hours: "))
wednesday2 = float(input("Enter overtiime 2.0 hours: "))
print("===============================================")
print()
print("==================THURSDAY=======================")
thursday = float(input("Enter normal day shift hours: "))
thursday_n = float(input("Enter normal night shift hours: "))
thursday1 = float(input("Enter overtiime 1.5 hours: "))
thursday2 = float(input("Enter overtiime 2.0 hours: "))
print("===============================================")
print()
print("==================FRIDAY=======================")
friday = float(input("Enter normal day shift hours: "))
friday_n = float(input("Enter normal night shift hours: "))
friday1 = float(input("Enter overtiime 1.5 hours: "))
friday2 = float(input("Enter overtiime 2.0 hours: "))
print("===============================================")
print()
print("==================SATURDAYDAY=======================")
saturday = float(input("Enter normal day shift hours: "))
saturday_n = float(input("Enter normal night shift hours: "))
saturday1 = float(input("Enter overtiime 1.5 hours: "))
saturday2 = float(input("Enter overtiime 2.0 hours: "))
print("===============================================")
print()


#calculating hours worked in total 
total_hours = monday + tuesday + wednesday + thursday + friday + saturday + \
			  monday1 + tuesday1 + wednesday1 + thursday1 + friday1 + saturday1 + \
			  sunday2 + monday2 + tuesday2 + wednesday2 + thursday2 + friday2 + saturday2 + \
			  monday_n + tuesday_n + wednesday_n + thursday_n + friday_n + saturday_n 

#calculating hours worked by day
total_hours_sunday = sunday2
total_hours_monday = monday + monday_n + monday1 + monday2
total_hours_tuesday = tuesday + tuesday_n + tuesday1 + tuesday2
total_hours_wednesday = wednesday + wednesday_n + wednesday1 + wednesday2
total_hours_thursday = thursday + thursday_n + thursday1 + thursday2
total_hours_friday = friday + friday_n + friday1 + friday2
total_hours_saturday = saturday + saturday_n + saturday1 + saturday2

#calculating wages based on rates
#-------------Sunday--------------
calculate_sunday2 = sunday2*47.2300

#-------------Monday--------------
calculate_monday = monday*26.2400
calculate_monday_n = monday_n*29.3900
calculate_monday1 = monday1*36.7300
calculate_monday2 = monday2*47.2300

#-------------Tuesday--------------
calculate_tuesday = tuesday*26.2400
calculate_tuesday_n = tuesday_n*29.3900
calculate_tuesday1 = tuesday1*36.7300
calculate_tuesday2 = tuesday2*47.2300

#-------------Wednesday--------------
calculate_wednesday = wednesday*26.2400
calculate_wednesday_n = wednesday_n*29.3900
calculate_wednesday1 = wednesday1*36.7300
calculate_wednesday2 = wednesday2*47.2300

#-------------Thursday--------------
calculate_thursday = thursday*26.2400
calculate_thursday_n = thursday_n*29.3900
calculate_thursday1 = thursday1*36.7300
calculate_thursday2 = thursday2*47.2300

#-------------Fridayday--------------
calculate_friday = friday*26.2400
calculate_friday_n = friday_n*29.3900
calculate_friday1 = friday1*36.7300
calculate_friday2 = friday2*47.2300

#-------------Saturday--------------
calculate_saturday = saturday*26.2400
calculate_saturday_n = saturday_n*29.3900
calculate_saturday1 = saturday1*36.7300
calculate_saturday2 = saturday2*47.2300

#adding total wages
total_wages = calculate_sunday2 + calculate_monday + calculate_monday_n + calculate_monday1 + calculate_monday2 + calculate_tuesday + calculate_tuesday_n + calculate_tuesday1 + calculate_tuesday2 + calculate_wednesday + calculate_wednesday_n + calculate_wednesday1 + calculate_wednesday2 + calculate_thursday + calculate_thursday_n + calculate_thursday1 + calculate_thursday2 + calculate_friday + calculate_friday_n + calculate_friday1 + calculate_friday2 + calculate_saturday + calculate_saturday_n + calculate_saturday1 + calculate_saturday2 

#printing payslip estimations
print()
print("===================================================================================")
print("Hours worked on Sunday:    ", sunday2)
print("-------------------------------------------------------------------------------------")
print("Hours worked on Monday:    ", monday + monday_n + monday1 + monday2)
print("-------------------------------------------------------------------------------------")
print("Hours worked on Tuesday:   ", tuesday + tuesday_n + tuesday1 + tuesday2)
print("-------------------------------------------------------------------------------------")
print("Hours worked on Wednesday: ", wednesday + wednesday_n + wednesday1 + wednesday2)
print("-------------------------------------------------------------------------------------")
print("Hours worked on Thursday:  ", thursday + thursday_n + thursday1 + thursday2)
print("-------------------------------------------------------------------------------------")
print("Hours worked on Friday:    ", friday + friday_n + friday1 + friday2)
print("-------------------------------------------------------------------------------------")
print("Hours worked on Saturday:  ", saturday + saturday_n + saturday1 + saturday2)
print("===================================================================================")
print()
print("Total hours worked: ",total_hours)
print("===================================================================================")
print()
print()
print("Gross Taxable Earnings: $", round(total_wages, 2))
print()
#calculate tax 
if total_wages > 357:
	print("===================================================================================")
	print("===================================================================================")
	print("ENTER AMOUNT IN TAX CALCULATOR IF TOTAL WAGE IS MORE THAN $356")
	print("===================================================================================")
	print("===================================================================================")
	tax = float(input("Enter tax amount: "))

else:
	tax = 0
print()
print()
print()
print()
print()
print("============================ PRINTING ESTIMATES ======================================")
print()
print()
print()
print("===================================================================================")
print("Hours worked on Sunday:       ", sunday2)
print("-------------------------------------------------------------------------------------")
print("Hours worked on Monday:       ", monday + monday_n + monday1 + monday2)
print("-------------------------------------------------------------------------------------")
print("Hours worked on Tuesday:      ", tuesday + tuesday_n + tuesday1 + tuesday2)
print("-------------------------------------------------------------------------------------")
print("Hours worked on Wednesday:    ", wednesday + wednesday_n + wednesday1 + wednesday2)
print("-------------------------------------------------------------------------------------")
print("Hours worked on Thursday:     ", thursday + thursday_n + thursday1 + thursday2)
print("-------------------------------------------------------------------------------------")
print("Hours worked on Friday:       ", friday + friday_n + friday1 + friday2)
print("-------------------------------------------------------------------------------------")
print("Hours worked on Saturday:     ", saturday + saturday_n + saturday1 + saturday2)
print("===================================================================================")
print()
print("Total hours worked:           ",total_hours)
print("===================================================================================")
print()
print()

#calculating travel allowence
travel_allowence = []

if total_hours_sunday > 0:

	print("Travel Allowence - Sunday:    ", travel)
	travel_allowence.append(travel)
	print("--------------------------------------------------------")

if total_hours_monday > 0:
	print("Travel Allowence - Monday:    ", travel)
	travel_allowence.append(travel)
	print("--------------------------------------------------------")

if total_hours_tuesday > 0:
	print("Travel Allowence - Tuesday:   ", travel)
	travel_allowence.append(travel)
	print("--------------------------------------------------------")

if total_hours_wednesday > 0: 
	print("Travel Allowence - Wednesday: ", travel)
	travel_allowence.append(travel)
	print("--------------------------------------------------------")

if total_hours_thursday > 0:
	print("Travel Allowence - Thursday:  ", travel)
	travel_allowence.append(travel)
	print("--------------------------------------------------------")

if total_hours_friday > 0:
	print("Travel Allowence - Friday:    ", travel)
	travel_allowence.append(travel)
	print("--------------------------------------------------------")

if total_hours_saturday > 0:
	print("Travel Allowence - Saturday:  ", travel)
	travel_allowence.append(travel)
	print("--------------------------------------------------------")

print()
#calculating meal allowence
meal_allowence = []

if total_hours_sunday >= 10:
	meal_allowence.append(meal)
	print("Meal   Allowence - Sunday:    ", meal)
	print("--------------------------------------------------------")

if total_hours_monday >= 10:
	print("Meal   Allowence - Monday:    ", meal)
	meal_allowence.append(meal)
	print("--------------------------------------------------------")

if total_hours_tuesday >= 10:
	print("Meal   Allowence - Tuesday:   ", meal)
	meal_allowence.append(meal)
	print("--------------------------------------------------------")

if total_hours_wednesday >= 10: 
	print("Meal   Allowence - Wednesday: ", meal)
	meal_allowence.append(meal)
	print("--------------------------------------------------------")

if total_hours_thursday >= 10:
	print("Meal   Allowence - Thursday:  ", meal)
	meal_allowence.append(meal)
	print("--------------------------------------------------------")

if total_hours_friday >= 10:
	print("Meal   Allowence - Friday:    ", meal)
	meal_allowence.append(meal)
	print("--------------------------------------------------------")

if total_hours_saturday >= 10:
	print("Meal   Allowence - Saturday:  ", meal)
	meal_allowence.append(meal)
	print("--------------------------------------------------------")


print("=========================================================")
allowences = sum(travel_allowence + meal_allowence)
print("Total Allowences:             ", allowences)
print("--------------------------------------------------------")
print()
print("=========================================================")
if tax > 0:
	pass
	print("Wages before tax: ", round(total_wages,2))
	print("--------------------------------------------------------")
	net_pay = (round(total_wages, 2) - tax)
	print("Wages after tax: ",net_pay) 
	print("--------------------------------------------------------")
else:
	print("--------------------------------------------------------")
	net_pay = (round(total_wages, 2) - tax)
	print("Net income: ",net_pay) 
	print("--------------------------------------------------------")
print()
print()
print("Adding allowences...")
print()
print()
final_amount = net_pay + allowences
print("--------------------------------------------------------")
print("Estimated total pay: ", round(final_amount,2) + allowences)
print("=========================================================")
print()
print()
print()
print()
print()

