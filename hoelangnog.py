import datetime
import time
import streamlit as st

today = datetime.date.today()
future = datetime.date(2023,3,4)
diff = future - today
st.write(f"tis nog {diff.days} dagen tot skiverlof")

sneeuw = st.button('Ik wil nu al sneeuw')
if sneeuw:
    st.snow()
