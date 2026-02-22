import streamlit as st
from pathlib import Path
import json
import random
import string

# ---------------------------
# Bank Class (same as original)
# ---------------------------
class bank:
    database = "data.json"
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            data = []
    except:
        data = []

    @classmethod
    def update(cls):
        with open(bank.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @staticmethod
    def generateACC():
        digit = random.choices(string.digits, k=4)
        alpha = random.choices(string.ascii_letters, k=4)
        acc = digit + alpha
        random.shuffle(acc)
        return "".join(acc)


# ---------------------------
# SESSION STATE
# ---------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None


# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="Bluecrest Bank", layout="centered", page_icon="🏦")


# ---------------------------
# MAIN INTERFACE (UNCHANGED)
# ---------------------------
st.image("bluecrest_logo.jng", width=750)

st.markdown("<h1 style='text-align:center;'>BLUECREST BANK</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Welcome! Trusted Banking, Secure Future.</h3>", unsafe_allow_html=True)

st.markdown("---")

option = st.radio(
    "I am a:",
    ("Existing User", "New User"),
    horizontal=True
)

# ---------------------------
# LOGIN SECTION (UNCHANGED)
# ---------------------------
if option == "Existing User":

    st.subheader("Login to Your Account")

    account_no = st.text_input("Enter Account Number")
    pin = st.text_input("Enter PIN", type="password")

    if st.button("Login"):

        user = next(
            (i for i in bank.data
             if i["accountno"] == account_no and i["pin"] == pin),
            None
        )

        if user:

            st.success(f"Welcome {user['name']}!")

            st.session_state.logged_in = True
            st.session_state.user = user

        else:
            st.error("Invalid Account Number or PIN")


# ---------------------------
# CREATE ACCOUNT (UNCHANGED)
# ---------------------------
else:

    st.subheader("Create a New Account")

    name = st.text_input("Enter your Name")
    age = st.number_input("Enter your Age", min_value=1)
    email = st.text_input("Enter your Email")
    pin = st.text_input("Enter your PIN", type="password")
    phone = st.text_input("Enter your Phone No")

    if st.button("Create Account"):

        if age > 18 and len(pin) == 4 and len(phone) == 10:

            acc = bank.generateACC()

            user = {
                "name": name,
                "age": age,
                "email": email,
                "pin": pin,
                "accountno": acc,
                "phon_no": phone,
                "balance": 0
            }

            bank.data.append(user)
            bank.update()

            st.success(f"Account Created! Account No: {acc}")

        else:
            st.error("Invalid credentials")


# ---------------------------
# SIDEBAR (NEW) - ONLY AFTER LOGIN
# ---------------------------
if st.session_state.logged_in:

    st.sidebar.title("Bluecrest Bank Menu")

    menu = st.sidebar.selectbox(
        "Select Action",
        [
            "Dashboard",
            "Deposit Money",
            "View Details",
            "Delete Account",
            "Logout"
        ]
    )

    user = st.session_state.user

    # Dashboard
    if menu == "Dashboard":
        st.sidebar.success("Dashboard opened")
        st.write(f"Name: {user['name']}")
        st.write(f"Account Number: {user['accountno']}")
        st.write(f"Balance: ₹ {user['balance']}")

    # Deposit
    elif menu == "Deposit Money":

        amount = st.sidebar.number_input("Enter Amount", min_value=1)

        if st.sidebar.button("Deposit"):

            user["balance"] += amount
            bank.update()

            st.sidebar.success("Money Deposited")

    # View Details
    elif menu == "View Details":

        st.sidebar.json(user)

    # Delete
    elif menu == "Delete Account":

        if st.sidebar.button("Confirm Delete"):

            bank.data.remove(user)
            bank.update()

            st.session_state.logged_in = False
            st.session_state.user = None

            st.sidebar.success("Account Deleted")

    # Logout
    elif menu == "Logout":

        st.session_state.logged_in = False
        st.session_state.user = None

        st.sidebar.success("Logged Out")


