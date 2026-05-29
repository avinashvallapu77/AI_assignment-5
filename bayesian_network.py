from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


# -----------------------------------
# Creating Bayesian Network Structure
# -----------------------------------

# Rain ----> Traffic
# Accident -> Traffic

model = BayesianNetwork([
    ('Rain', 'Traffic'),
    ('Accident', 'Traffic')
])


# -----------------------------------
# Defining Conditional Probability Tables
# -----------------------------------

# Probability of Rain
cpd_rain = TabularCPD(
    variable='Rain',
    variable_card=2,
    values=[
        [0.7],   # No Rain
        [0.3]    # Rain
    ]
)

# Probability of Accident
cpd_accident = TabularCPD(
    variable='Accident',
    variable_card=2,
    values=[
        [0.8],   # No Accident
        [0.2]    # Accident
    ]
)

# Probability of Traffic given Rain and Accident
cpd_traffic = TabularCPD(
    variable='Traffic',
    variable_card=2,

    values=[
        # No Traffic
        [0.9, 0.6, 0.7, 0.1],

        # Traffic
        [0.1, 0.4, 0.3, 0.9]
    ],

    evidence=['Rain', 'Accident'],
    evidence_card=[2, 2]
)


# -----------------------------------
# Adding CPDs to Model
# -----------------------------------

model.add_cpds(
    cpd_rain,
    cpd_accident,
    cpd_traffic
)


# -----------------------------------
# Checking Model Validity
# -----------------------------------

print("Is Bayesian Network Valid?")
print(model.check_model())


# -----------------------------------
# Performing Inference
# -----------------------------------

infer = VariableElimination(model)


# Query 1
print("\n-----------------------------------")
print("Probability Distribution of Traffic")
print("-----------------------------------")

result1 = infer.query(variables=['Traffic'])

print(result1)


# Query 2
print("\n-----------------------------------")
print("Probability of Traffic Given Rain")
print("-----------------------------------")

result2 = infer.query(
    variables=['Traffic'],
    evidence={'Rain': 1}
)

print(result2)


# Query 3
print("\n-----------------------------------")
print("Probability of Traffic Given Rain and Accident")
print("-----------------------------------")

result3 = infer.query(
    variables=['Traffic'],
    evidence={
        'Rain': 1,
        'Accident': 1
    }
)

print(result3)


# -----------------------------------
# Displaying CPDs
# -----------------------------------

print("\n-----------------------------------")
print("Conditional Probability Tables")
print("-----------------------------------")

print(cpd_rain)
print(cpd_accident)
print(cpd_traffic)


# -----------------------------------
# End of Program
# -----------------------------------

print("\nBayesian Network Modelling and Inference Completed Successfully")
