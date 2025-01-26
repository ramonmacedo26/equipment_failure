# equipment_failure
This app calculates and visualizes probabilities of equipment failures based on the Poisson distribution. It is designed to help users understand the likelihood of specific failure events over a given period.

What the App Does

Calculations with the Poisson Distribution:

Exact Probability: Computes the probability of a specific number of failures occurring (e.g., exactly 3 failures).

Cumulative Probability (Less Than or Equal): Calculates the probability of having a certain number of failures or fewer (e.g., up to 3 failures).

Complementary Probability (Greater Than): Computes the probability of experiencing more than a certain number of failures (e.g., more than 3 failures).

Dynamic Visualizations:

The app generates bar charts to display the probabilities for different failure occurrences.
Labels on the bars include both the occurrence count and its probability percentage for better clarity.

Interactive Inputs:

Users can input the average rate of occurrences (λ) to customize the calculations.
They can also define an interval to visualize probabilities around the expected value.
A sidebar allows users to select the type of calculation and modify parameters in real time.
Tabular Data:

Probabilities are displayed in a table alongside the graph for easy interpretation.

Who Is It For?
This app is useful for:

Reliability engineers analyzing equipment failure rates.
Statisticians and data scientists exploring Poisson-distributed phenomena.
Educators and students learning about probability and the Poisson distribution.

Check it out https://equipmentfailure.streamlit.app/
