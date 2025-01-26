import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Page configuration
st.set_page_config(page_title="Equipment Failure Probability", layout="wide")

st.title("Equipment Failure Probability")

# Sidebar configuration
with st.sidebar:
    st.header("Settings")
    calc_type = st.radio("Select Calculation Type", options=["Exact Prob.", "Less Than or Equal", "Greater Than"])
    occurrence = st.number_input("Average Occurrence (λ)", min_value=1, max_value=99, value=2, step=1)
    interval = st.slider("Define the interval around λ", min_value=1, max_value=10, value=2)

# Automatic calculation
lamb = occurrence
start = lamb - interval
end = lamb + interval
x_vals = np.arange(max(0, start), end + 1)  # Ensure non-negative values

if calc_type == "Exact Prob.":
    probs = poisson.pmf(x_vals, lamb)
    title = "Exact Probability"
elif calc_type == "Less Than or Equal":
    probs = poisson.cdf(x_vals, lamb)
    title = "Cumulative Probability (≤)"
else:
    probs = poisson.sf(x_vals, lamb)
    title = "Complementary Probability (>)"

# Formatted results
z_vals = np.round(probs, 4)
labels = [f"{i} ({p:.2%})" for i, p in zip(x_vals, z_vals)]

# Visualization - Bar Chart
fig, ax = plt.subplots(figsize=(5, 5))
ax.bar(x_vals, probs, tick_label=labels, color=plt.cm.viridis(np.linspace(0.4, 0.8, len(x_vals))))
ax.set_title(title)
ax.set_xlabel("Number of Occurrences")
ax.set_ylabel("Probability")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)

# Display Table
st.subheader("Probability Table")
st.dataframe({"Occurrences": x_vals, "Probabilities": z_vals})
