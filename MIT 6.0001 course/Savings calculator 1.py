annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:  "))


total_cost = int(input("Enter the cost of your dream home "))

semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

portion_down_payment = total_cost * 0.25

monthly_salary = annual_salary / 12
monthly_saved = monthly_salary * portion_saved


current_savings = 0.0
annual_return = 0.04 
monthly_return = annual_return / 12
months = 0 

while current_savings < portion_down_payment:
    months += 1
    current_savings *= 1 + monthly_return
    current_savings +=  monthly_return 
    if months % 6 == 0: 
        annual_salary *= 1 + semi_annual_raise
        monthly_saved = (annual_salary / 12.0) * portion_saved
      
print("Number of months: ", months)