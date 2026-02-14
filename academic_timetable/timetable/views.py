from django.shortcuts import render


def timetable_view(request):
    student = {
        "name": "Alice Johnson",
        "branch": "Computer Science",
        "year": "3rd Year",
    }

    weekly_timetable = {
        "Monday": [
            {"time": "09:00 - 10:00", "subject": "Discrete Math", "room": "A101", "teacher": "Dr. Rao"},
            {"time": "10:00 - 11:00", "subject": "Data Structures", "room": "A202", "teacher": "Prof. Kim"},
            {"time": "11:15 - 12:15", "subject": "Operating Systems", "room": "B305", "teacher": "Dr. Singh"},
            {"time": "13:15 - 14:15", "subject": "Elective: AI", "room": "Lab-2", "teacher": "Dr. Patel"},
        ],
        "Tuesday": [
            {"time": "09:00 - 10:00", "subject": "Computer Networks", "room": "A105", "teacher": "Dr. Chen"},
            {"time": "10:10 - 11:10", "subject": "Database Systems", "room": "A206", "teacher": "Prof. Lee"},
            {"time": "11:20 - 12:20", "subject": "Software Engineering", "room": "B303", "teacher": "Dr. Brown"},
            {"time": "13:20 - 14:20", "subject": "Elective: ML", "room": "Lab-1", "teacher": "Dr. Patel"},
        ],
        "Wednesday": [
            {"time": "09:00 - 10:00", "subject": "Algorithms", "room": "A107", "teacher": "Dr. Gupta"},
            {"time": "10:10 - 11:10", "subject": "Cloud Computing", "room": "A210", "teacher": "Ms. Davis"},
            {"time": "11:20 - 12:20", "subject": "Compiler Design", "room": "B301", "teacher": "Dr. White"},
            {"time": "13:20 - 14:20", "subject": "Elective: NLP", "room": "Lab-3", "teacher": "Dr. Patel"},
        ],
        "Thursday": [
            {"time": "09:00 - 10:00", "subject": "Distributed Systems", "room": "A109", "teacher": "Dr. Young"},
            {"time": "10:10 - 11:10", "subject": "Cyber Security", "room": "A212", "teacher": "Dr. King"},
            {"time": "11:20 - 12:20", "subject": "Human-Computer Interaction", "room": "B302", "teacher": "Ms. Clark"},
            {"time": "13:20 - 14:20", "subject": "Project Lab", "room": "Lab-4", "teacher": "Mentors"},
        ],
        "Friday": [
            {"time": "09:00 - 10:00", "subject": "Numerical Methods", "room": "A111", "teacher": "Dr. Hall"},
            {"time": "10:10 - 11:10", "subject": "Advanced Python", "room": "A214", "teacher": "Mr. Allen"},
            {"time": "11:20 - 12:20", "subject": "IoT Fundamentals", "room": "B304", "teacher": "Ms. Baker"},
            {"time": "13:20 - 14:20", "subject": "Seminar", "room": "Auditorium", "teacher": "Guest"},
        ],
    }

    context = {"student": student, "weekly_timetable": weekly_timetable}
    return render(request, "timetable/timetable.html", context)
