from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user-authentication')
def user_authentication():
    return render_template('user_authentication.html')

@app.route('/patient-management')
def patient_management():
    return render_template('pmanagement.html')

@app.route('/treatment-management')
def treatment_management():
    return render_template('treatment_management.html')

@app.route('/task-management')
def task_management():
    return render_template('task_management.html')

@app.route('/payment-handling')
def payment_handling():
    return render_template('payment_handling.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/campaign-management')
def campaign_management():
    return render_template('campaign_management.html')

@app.route('/automated-follow-ups')
def automated_follow_ups():
    return render_template('automated_follow_ups.html')

@app.route('/analytics-dashboard')
def analytics_dashboard():
    kpi_data = {
        'production_metrics': 30000,
        'treatment_acceptance_rate': 85,
        'accounts_receivable': 12000,
        'appointments_today': 10,
        'new_patients': 5,
        'months': ['January', 'February', 'March', 'April', 'May', 'June'],
        'production_metrics_over_time': [10000, 15000, 20000, 25000, 30000, 35000],
        'accounts_receivable_over_time': [20000, 18000, 16000, 14000, 12000, 10000]
    }
    return render_template('analytics_dashboard.html', kpi_data=kpi_data)

@app.route('/workflow-automation')
def workflow_automation():
    return render_template('workflow_automation.html')

if __name__ == '__main__':
    app.run(debug=True)
