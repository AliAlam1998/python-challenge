# Dependencies
import os
import csv

# Set the path to the budget data CSV file
csvpath = "Resources\\budget_data.csv"

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
profit_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    csv_header = next(csvreader)
    
    # Loop through the rows
    for row in csvreader:
        # Extract data from the row
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculate the total months and net total
        total_months += 1
        net_total += profit_loss
        
        # Calculate the profit change
        if total_months > 1:
            change = profit_loss - previous_profit
            profit_changes.append(change)
            
            # Check for greatest increase and decrease
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]
        
        # Update previous profit for the next iteration
        previous_profit = profit_loss

# Calculate the average change
average_change = round(sum(profit_changes) / len(profit_changes), 2)

# Print results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export results to a text file
output_path ="Analysis\\Financial_analysis.txt"
with open(output_path, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total}\n")
    textfile.write(f"Average Change: ${average_change}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
