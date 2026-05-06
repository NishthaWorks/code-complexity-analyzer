print("Paste your code (type END in new line to finish):")

lines = []

# Multi-line input
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

# Variables
stack = []
max_depth = 0
loop_types = []
function_names = []
recursion_detected = False
binary_search_detected = False

# Process each line
for line in lines:
    stripped = line.lstrip()

    # 🔹 Detect function definitions
    if stripped.startswith("def"):
        func_name = stripped.split()[1].split("(")[0]
        function_names.append(func_name)

    # 🔹 Detect recursion
    for func in function_names:
        if func + "(" in stripped:
            recursion_detected = True

    # 🔹 Detect binary search pattern
    if "while" in stripped and "low" in stripped and "high" in stripped:
        binary_search_detected = True

    # 🔹 Detect loops
    if stripped.startswith(("for", "while")):
        indent = len(line) - len(stripped)

        while stack and indent <= stack[-1]:
            stack.pop()

        stack.append(indent)
        max_depth = max(max_depth, len(stack))
        loop_types.append(stripped.split()[0])

loop_count = len(loop_types)

print("\n--- Analysis ---")

# 🔥 Priority order

if binary_search_detected:
    print("Time Complexity: O(log n)")
    print("Reason: Binary search pattern detected")
    print("Suggestion: Ensure array is sorted for correctness")

elif recursion_detected:
    print("Time Complexity: Depends on recursion (often O(n))")
    print("Reason: Recursive function detected")
    print("Suggestion: Check base condition and recursion depth")

elif loop_count == 0:
    print("Time Complexity: O(1)")
    print("Suggestion: Code is efficient 👍")

elif max_depth == 1:
    print("Time Complexity: O(n)")
    print("Reason: Single level loop")
    print("Suggestion: Try reducing iterations if possible")

elif max_depth >= 2:
    print(f"Time Complexity: O(n^{max_depth})")
    print(f"Reason: {max_depth} levels of nested loops detected")

    if "while" in loop_types:
        print("Suggestion: Optimize conditions or break early")
    else:
        print("Suggestion: Use better data structures to reduce nesting")