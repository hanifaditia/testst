import streamlit as st
import pandas as pd

# Sample DataFrame initialization (Replace with your actual DataFrame)
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar'],
        'Realisasi': [0, 0, 0],
        'Target': [0, 0, 0],
        'Cumul_Realisasi': [0, 0, 0],
        'Cumul_Target': [0, 0, 0],
        'Monthly_Ach': [0, 0, 0],
        'Quarterly_Ach': [0, 0, 0],
        'Cumul_quarterly': [0, 0, 0],
        'Cumul_vs_Yearly': [0, 0, 0],
    })

# Initialize session state for menu selection
if 'selected_menu' not in st.session_state:
    st.session_state.selected_menu = 'All Company'

# Sidebar menu
menu_options = ['All Company', 'Accenture', 'IBM', 'Alibaba', 'PaloAlto Networks', 'Cisco', 'Meta', 'Thales']
st.session_state.selected_menu = st.sidebar.selectbox(
    'Menu', 
    menu_options,
    index=menu_options.index(st.session_state.selected_menu)
)

dic = {"test" : st.secrets.test}

st.markdown(str(st.secrets.test))
st.markdown("dict")
st.markdown(dic)
st.markdown(dic["test"])

# Sort the DataFrame
st.session_state.df = st.session_state.df.sort_values('Month')

# Function to display 'All Company' section
def display_all_company(df = st.session_state.df):
    st.markdown("## Summary All Company GSP")
    
    # df = st.session_state.df  # Use the DataFrame from session state
    
    # # Ensure the cumulative yearly achievement values for the latest and previous month
    # latest_cumulative_yearly = df['Cumul_vs_Yearly'].iloc[-1] if pd.notna(df['Cumul_vs_Yearly'].iloc[-1]) else 0
    # previous_cumulative_yearly = df['Cumul_vs_Yearly'].iloc[-2] if pd.notna(df['Cumul_vs_Yearly'].iloc[-2]) else 0

    # # Calculate the percentage change in cumulative yearly achievement
    # if previous_cumulative_yearly != 0:
    #     cumulative_yearly_change = ((latest_cumulative_yearly - previous_cumulative_yearly) / previous_cumulative_yearly) * 100
    # else:
    #     cumulative_yearly_change = 0  # To avoid division by zero if there's no previous data

    # # Compact metrics boxes for Cumulative Yearly Achievement Change
    # col3 = st.columns(1)[0]
    
    # with col3:
    #     st.metric(
    #         label="Cumulative Yearly Achievement", 
    #         value=f"{latest_cumulative_yearly:.2f}%", 
    #         delta=f"{cumulative_yearly_change:.2f}%"
    #     )

    # st.markdown("""---------""")

    # Format the required columns before displaying the dataframe
    df_style = df.style.format({
        'Realisasi': '{:.2f}', 
        'Target': '{:.2f}', 
        'Cumul_Realisasi': '{:.2f}', 
        'Cumul_Target': '{:.2f}', 
        'Monthly_Ach': '{:.2f}%', 
        'Quarterly_Ach': '{:.2f}%', 
        'Cumul_quarterly': '{:.2f}%', 
        'Cumul_vs_Yearly': '{:.2f}%'
    })

    # Display the styled dataframe
    st.dataframe(df_style, use_container_width=True)

# Show the 'All Company' section if selected
# if st.session_state.selected_menu == 'All Company':
#     display_all_company()

# Form for updating DataFrame (example)


# Display the selected menu section based on the session state
if st.session_state.selected_menu == 'All Company':
    with st.sidebar.form("Update Form"):
        Month = st.selectbox("Month", st.session_state.df['Month'].tolist())
        Realisasi = st.number_input("Realisasi", value=0.0) 
        Target = st.number_input("Target", value=0.0) 
        submit = st.form_submit_button("Update Data")

        if submit:
            # Update the DataFrame
            df = st.session_state.df
            df.loc[df['Month'] == Month, 'Realisasi'] = float(Realisasi)
            df.loc[df['Month'] == Month, 'Target'] = float(Target)
            
            # Update the session state
            st.session_state.df = df
            
            # Set the menu back to 'All Company' to refresh the display
            st.session_state.selected_menu = 'All Company'
            
            # Optional: Show a success message
            st.success(f"Data updated for {Month}: Realisasi = {Realisasi}, Target = {Target}")
    display_all_company()
elif st.session_state.selected_menu == 'Accenture':
    df = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar'],
        'Realisasi': [0, 0, 0],
        'Target': [0, 0, 0],
        'Cumul_Realisasi': [0, 0, 0],
        'Cumul_Target': [0, 0, 0],
        'Monthly_Ach': [0, 0, 0],
        'Quarterly_Ach': [0, 0, 0],
        'Cumul_quarterly': [0, 0, 0],
        'Cumul_vs_Yearly': [0, 0, 0],
    })
    with st.sidebar.form("Update Form"):
        Month = st.selectbox("Month", st.session_state.df['Month'].tolist())
        Realisasi = st.number_input("Realisasi", value=0.0) 
        Target = st.number_input("Target", value=0.0) 
        submit = st.form_submit_button("Update Data")

        if submit:
            # Update the DataFrame
            df = st.session_state.df
            df.loc[df['Month'] == Month, 'Realisasi'] = float(Realisasi)
            df.loc[df['Month'] == Month, 'Target'] = float(Target)
            
            # Update the session state
            st.session_state.df = df
            
            # Set the menu back to 'All Company' to refresh the display
            st.session_state.selected_menu = 'All Company'
            
            # Optional: Show a success message
            st.success(f"Data updated for {Month}: Realisasi = {Realisasi}, Target = {Target}")
    display_all_company(df)
