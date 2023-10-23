from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    start_hour = int(request.form['start_hour'])
    start_minute = int(request.form['start_minute'])
    start_period = request.form['start_period']

    lunch_start_hour = int(request.form['lunch_start_hour'])
    lunch_start_minute = int(request.form['lunch_start_minute'])
    lunch_start_period = request.form['lunch_start_period']

    lunch_end_hour = int(request.form['lunch_end_hour'])
    lunch_end_minute = int(request.form['lunch_end_minute'])
    lunch_end_period = request.form['lunch_end_period']

    if start_period == 'PM':
        start_hour += 12

    if lunch_start_period == 'PM':
        lunch_start_hour += 12

    if lunch_end_period == 'PM':
        lunch_end_hour += 12

    start_time = datetime(year=2023, month=1, day=1, hour=start_hour, minute=start_minute)
    lunch_start_time = datetime(year=2023, month=1, day=1, hour=lunch_start_hour, minute=lunch_start_minute)
    lunch_end_time = datetime(year=2023, month=1, day=1, hour=lunch_end_hour, minute=lunch_end_minute)

    work_hours = (lunch_start_time - start_time) + (lunch_end_time - lunch_start_time)

    work_before_lunch = lunch_start_time - start_time

    work_after_lunch = timedelta(hours=9) - work_hours

    if work_hours.total_seconds() < 8 * 3600:  # If total work hours are less than 8 hours
        leave_time = lunch_end_time + work_after_lunch

        result = leave_time.strftime('%I:%M %p')
    else:
        result = "You have already worked 8 hours or more."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
