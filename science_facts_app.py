import streamlit as st
import random

# Science facts dictionary
science_facts = {
    "Space": [
        "A day on Venus is longer than a year on Venus.",
        "Neutron stars can spin 600 times per second.",
        "There’s floating water in space.",
    ],
    "Biology": [
        "Your body has more bacteria than human cells.",
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries aren't.",
    ],
    "Chemistry": [
        "Water can boil and freeze at the same time.",
        "Helium can work against gravity and escape Earth.",
        "Glass is actually a very slow-moving liquid.",
    ],
    "Physics": [
        "Light behaves both like a particle and a wave.",
        "Time moves slower near massive objects.",
        "Absolute zero is the coldest possible temperature.",
    ]
}

# Streamlit app
st.title("🔬 Quick Science Facts Generator")
st.write("Select a science topic and get a random fact!")

topic = st.selectbox("Choose a topic:", list(science_facts.keys()))

if st.button("Give me a fact!"):
    fact = random.choice(science_facts[topic])
    st.success(fact)
