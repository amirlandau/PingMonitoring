from website import create_app
from apscheduler.schedulers.background import BackgroundScheduler
from website.jobs import update_ip_status


app = create_app()


if __name__ == '__main__':
    # Ping all IP addresses every 15 seconds in the background.
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=update_ip_status, trigger="interval", seconds=15)
    scheduler.start()

    app.run(debug=True,host='0.0.0.0')


