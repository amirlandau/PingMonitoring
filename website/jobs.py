from .models import Servers
from . import db, create_app
import concurrent.futures
from datetime import datetime
from .functions import reliable_ping


app = create_app()


# Update servers IP status.
def update_ip_status():
    with app.app_context():
        ip_list = [
            server.ip for server in Servers.query.with_entities(Servers.ip)]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            check_status = dict(
                (executor.submit(reliable_ping, ip), ip) for ip in ip_list)

            """Creates a dictionary of IP : Status
            check_status[future] = ip,  future.result() = status"""
            ip_and_status_dict = {check_status[future]: future.result(
            ) for future in concurrent.futures.as_completed(check_status)}
            
        # Updating IP server status.
        for ip, status in ip_and_status_dict.items():
            server = Servers.query.filter(Servers.ip == ip).first()
            previous_status = server.status
            server.status = status
            updated_status = server.status


            # Updating date only when IP server status changes.
            if previous_status == "0" and updated_status == True or previous_status == "1" and updated_status == False:
                server.status_date = datetime.now()

        db.session.commit()
