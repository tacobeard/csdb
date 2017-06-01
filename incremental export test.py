import zenpy, datetime, zdcreds

zenpy_client = zenpy.Zenpy(**zdcreds.creds)

 
last_hour = datetime.datetime.now() - datetime.timedelta(hours=1)
result_generator = zenpy_client.tickets.incremental(start_time=last_hour)


for ticket in zenpy_client.tickets.incremental(start_time=last_hour):
    for field in ticket.custom_fields:
        if field['id'] == 29655218:
            print(str(ticket.id)+' '+str(field['value'])+' '+str(ticket.tags)+' '+str(ticket.group_id)+' '+str(ticket.created_at)+' '+str(ticket.updated_at))
