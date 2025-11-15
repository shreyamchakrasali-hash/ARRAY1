import sys

# MAIN BRANCH FUNCTIONALITY:
# Sum & Average only

# Example run:
# python array_scores.py 10 20 30 40

if len(sys.argv) > 1:
    scores = sys.argv[1:]          # Read from command-line arguments
    print("User provided input values:")
else:
    print("No command-line input provided. Using default values:")
    scores = ["10", "20", "30", "40"]   # Default scores

# Using eval() for calculations
total = sum(eval(x) for x in scores)
average = total / len(scores)

print("Sum of scores =", total)
print("Average of scores =", average)