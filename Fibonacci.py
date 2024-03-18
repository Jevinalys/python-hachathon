## Functions & Fibonacci Sequence
# Question
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
#We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.
def fibonacci(n):
  generatedFibonacci=[0,1]

  if n <= 1:
    return generatedFibonacci
  
  else:
    while len(generatedFibonacci) < n:
      next_term =generatedFibonacci[-1]+generatedFibonacci[-2]
      generatedFibonacci.append(next_term)

    return generatedFibonacci

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

print(fibonacci(num_terms))
