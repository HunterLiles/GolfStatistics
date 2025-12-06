import streamlit as st

left_column, right_column = st.columns(2)

conn = st.connection("golf_db", type="sql")

ColumnOption1 = left_column.selectbox(
    "Select option",
    conn.query("SELECT RoundID, CourseID FROM GolfRound").columns
)

if ColumnOption1 == "CourseID":
    with st.spinner("Calculating Handicap"):
        st.write("You selected: ", ColumnOption1)
        st.dataframe(conn.query("SELECT CourseName FROM Course"))
if ColumnOption1 == "RoundID":
    with st.spinner("Calculating Handicap"):
        st.write("You selected: ", ColumnOption1)
        st.dataframe(conn.query("SELECT RoundID, RoundScore, RoundDate, CourseName"
                                " FROM GolfRound GR "
                                "JOIN Course C ON GR.CourseID = C.CourseID"))


CalculateHCButton = st.button("Calculate Handicap")
if CalculateHCButton:
    with st.spinner("Calculating Handicap"):
        df = conn.query("EXEC HCCalculation")
        result = df.iloc[0,0]
        st.write(result)
