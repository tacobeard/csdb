import zenpy, datetime, zdcreds

zenpy_client = zenpy.Zenpy(**zdcreds.creds)

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
result_generator = zenpy_client.tickets.incremental(start_time=yesterday)

for ticket in result_generator:
    print(str(ticket.id)+' '+str(ticket.tags)+' '+str(ticket.group_id)+' '+str(ticket.created_at)+' '+str(ticket.updated_at))

