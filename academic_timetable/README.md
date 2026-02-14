# Academic Timetable (Django)

A simple Django project that displays an academic timetable with student `name`, `branch`, and `year`, followed by a weekly schedule. Data is passed from the view into the template.

## Setup (Windows)

```powershell
# from this folder
cd academic_timetable

# (optional) create & activate venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt

# initial migrations
python manage.py migrate

# run server
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the timetable.

## Structure

- `manage.py` – Django management
- `academic_timetable/` – project settings & URLs
- `timetable/` – app with views and app URLs
- `templates/timetable/timetable.html` – UI template
- `static/css/styles.css` – styling

## Customize Data
Edit `timetable/views.py` and change the `student` dict and `weekly_timetable` entries as needed.
