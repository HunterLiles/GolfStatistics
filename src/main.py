import streamlit as st
from sqlalchemy import text

# Makes two columns that splits the screen down the middle
left_column, right_column = st.columns(2)

# Sets the connection to the database
conn = st.connection("golf_db", type="sql")

left_column.title('My Golf Data')
left_column.divider()
st.sidebar.title('Golf Statistics')

# Function that allows you to see GolfRound table and Course table.
@st.fragment()
def view_rounds():
    if st.button("Refresh"): pass

    st.dataframe(conn.query("SELECT RoundID, RoundScore, RoundDate, CourseName "
                            "FROM GolfRound GR "
                            "JOIN Course C ON GR.CourseID = C.CourseID", ttl=1))

    st.dataframe(conn.query("SELECT CourseName FROM Course", ttl=1))

view_rounds()

st.sidebar.divider()

st.sidebar.subheader('Add/Remove Rounds')

addRoundButton = st.sidebar.button("Add Round")
removeRoundButton = st.sidebar.button("Remove Round")

# A function that allows me to add a score to the database by brining up a tab that
# allows you to put in a score, course, and date and then adds that to the database.
@st.dialog("Add Round")
def addRound():
    roundscore = st.number_input("Round Score", value=72, step=1)
    coursename = st.text_input("Course Name")
    rounddate = st.date_input("Round Date")

    if st.button("Add Round"):
        with conn.session as s:
            query = text("EXEC InsertRound @RoundScore = :score, @CourseName = :course, @RoundDate = :date")

            params = {
                "score": roundscore,
                "course": coursename,
                "date": rounddate
            }

            s.execute(query, params)
            s.commit()

        st.success("Round Added")

# Same kind of function as the last one but instead of adding it removes. Same logic to make that happen
@st.dialog("Remove Round")
def removeRound():
    roundid = st.number_input("Round ID", value=1, step=1)
    rounddate = st.date_input("Round Date")
    coursename = st.text_input("Course Name")

    if st.button("Remove Round"):
        with conn.session as s:
            query = text("EXEC DeleteRound @RoundID = :id, @RoundDate = :date,@CourseName = :course")

            params = {
                "id": roundid,
                "date": rounddate,
                "course": coursename
            }

            s.execute(query, params)
            s.commit()

        st.success("Round Removed")


if addRoundButton:
    addRound()

if removeRoundButton:
    removeRound()

st.sidebar.divider()

st.sidebar.subheader('Handicap')

# Calls a stored procedure in the database to calculate the handicap.
CalculateHCButton = st.sidebar.button("Calculate Handicap")
if CalculateHCButton:
    with st.spinner("Calculating Handicap"):
        df = conn.query("EXEC HCCalculation")
        result = df.iloc[0, 0]
        st.sidebar.write(result)