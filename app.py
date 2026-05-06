import streamlit as st

# Page config
st.set_page_config(page_title="Code Analyzer", page_icon="💻", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💻 Code Complexity Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Analyze your code complexity instantly 🚀</p>", unsafe_allow_html=True)

# Input box
user_code = st.text_area("📌 Paste your code below:", height=200)

# Button
if st.button("🔍 Analyze Code"):

    lines = user_code.split("\n")

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

        if stripped.startswith("def"):
            func_name = stripped.split()[1].split("(")[0]
            function_names.append(func_name)

        for func in function_names:
            if func + "(" in stripped:
                recursion_detected = True

        if "while" in stripped and "low" in stripped and "high" in stripped:
            binary_search_detected = True

        if stripped.startswith(("for", "while")):
            indent = len(line) - len(stripped)

            while stack and indent <= stack[-1]:
                stack.pop()

            stack.append(indent)
            max_depth = max(max_depth, len(stack))
            loop_types.append(stripped.split()[0])

    loop_count = len(loop_types)

    st.markdown("---")
    st.subheader("📊 Analysis Result")

    # Output with styling
    if binary_search_detected:
        st.success("🚀 Time Complexity: O(log n)")
        st.info("Reason: Binary search pattern detected")

    elif recursion_detected:
        st.warning("⚠️ Time Complexity: Depends on recursion (often O(n))")
        st.info("Reason: Recursive function detected")

    elif loop_count == 0:
        st.success("✅ Time Complexity: O(1)")

    elif max_depth == 1:
        st.success("📈 Time Complexity: O(n)")
        st.info("Reason: Single level loop")

    else:
        st.error(f"🔥 Time Complexity: O(n^{max_depth})")
        st.info(f"Reason: {max_depth} levels of nested loops detected")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)