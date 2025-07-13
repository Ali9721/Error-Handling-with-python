# Define "numerator" & "denominator" & "result" as variables & use "try"
try:
    numerator   = int(input("please enter a numberaot: "))
    denominator = int(input("please enter a denominator: "))
    result      =  numerator / denominator

# Define "ZeroDivisionError" to avoid divide by zero & use "except" & output the result in this condition.
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

# Define "ValueError" to use a valid integer & use "except" & output the result in this condition.
except ValueError:
    print("Error: Invalid input, please enter a valid integer.")

# Use "else" & output the result in this condition.
else:
    print(f"Result: {result}")

# Use "finally" & output the result in this condition.
finally:
    print("Execution completed!")