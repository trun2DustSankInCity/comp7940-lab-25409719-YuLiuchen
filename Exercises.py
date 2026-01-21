# Exercise 1,2: Factors Function
def print_factor(x:int):
    factors = []
    for i in range(2,x):
        if x%i == 0:
            factors.append(i)
    print(f"All factors of {x} are: {factors}\n")
x = 52633
print_factor(x)
# Exercise 2,3: List Iteration
def print_factors_from_list(arr:list[int]):
    factors_dict = {}
    print("Exercise 3 started!")
    for element in arr:
        factors_dict[element] = []
        for i in range(2, element):
            if element%i == 0:
                factors_dict[element].append(i)
        print(f"All factors of {element} are: {factors_dict[element]}")
l = [52633, 8137, 1024, 999]
print_factors_from_list(l)

# make a conflect by branch