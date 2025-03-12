import streamlit as st
import zxcvbn
import re

# Function to check password strength
def check_password_strength(password):
    if not password:
        return "Please enter a password.", 0
    
    strength = zxcvbn.zxcvbn(password)
    score = strength["score"]
    
    feedback = strength["feedback"]["suggestions"]
    feedback = "\n".join(feedback) if feedback else "Strong password!"
    
    return feedback, score

# Streamlit UI
st.set_page_config(page_title="Advanced Password Strength Checker", page_icon="🔐")

st.title("🔐 Advanced Password Strength Checker")
st.markdown("Check the strength of your password in real time.")

password = st.text_input("Enter your password", type="password")

if password:
    feedback, score = check_password_strength(password)

    # Password Strength Bar
    st.progress(score / 4) 

    # Display Feedback
    if score == 0:
        st.error(f"❌ Weak Password! \n{feedback}")
    elif score == 1:
        st.warning(f"⚠️ Fair Password! \n{feedback}")
    elif score == 2:
        st.info(f"🟡 Moderate Password! \n{feedback}")
    elif score == 3:
        st.success(f"✅ Strong Password! \n{feedback}")
    elif score == 4:
        st.success("🔥 Very Strong Password! Well done!")

# Footer
st.markdown("""
---
💻 **Developed by Usman Gini Technology**  
""")
