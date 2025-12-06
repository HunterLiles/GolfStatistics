import streamlit as st
from sqlalchemy import text

left_column, right_column = st.columns(2)

conn = st.connection("golf_db", type="sql")

left_column.title('Golf Stuff')
left_column.divider()
st.sidebar.title('Golf Statistics')

st.sidebar.subheader('Tables')

ColumnOption1 = st.sidebar.selectbox(
    "Select option",
    conn.query("SELECT RoundID AS 'Round', CourseID AS 'Course Names' FROM GolfRound").columns
)


@st.fragment()
def view_rounds():
    if st.button("Refresh"): pass

    if ColumnOption1 == "Course Names":
        with st.spinner("Figuring stuff out..."):
            st.write(ColumnOption1)
            st.dataframe(conn.query("SELECT CourseName FROM Course", ttl=1))

    if ColumnOption1 == "Round":
        with st.spinner("Figuring stuff out..."):
            st.write(ColumnOption1)
            st.dataframe(conn.query("SELECT RoundID, RoundScore, RoundDate, CourseName "
                                    "FROM GolfRound GR "
                                    "JOIN Course C ON GR.CourseID = C.CourseID", ttl=1))

view_rounds()

st.sidebar.divider()

st.sidebar.subheader('Add/Remove Rounds')

addRoundButton = st.sidebar.button("Add Round")
removeRoundButton = st.sidebar.button("Remove Round")


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

CalculateHCButton = st.sidebar.button("Calculate Handicap")
if CalculateHCButton:
    with st.spinner("Calculating Handicap"):
        df = conn.query("EXEC HCCalculation")
        result = df.iloc[0, 0]
        st.sidebar.write(result)