import zenpy, datetime, zdcreds #,pytz

#authenticate with Zendesk client
zenpy_client = zenpy.Zenpy(**zdcreds.creds)

#reads end time of last export, to be used as start time for new export
with open("export_time.txt","r") as f:
    export_time = f.read()

#yesterday = datetime.datetime.now(pytz.utc) - datetime.timedelta(days=1)
result_generator = zenpy_client.tickets.incremental(start_time=int(export_time))

# Pulls ticket data and manually formats into SQL syntax
# Output columns are ordered as follows: platform, player_id, location, ticket_id, ticket_tags, group, ticket_created, last_update
custom = ''
data = ''
for ticket in result_generator:
    for field in ticket.custom_fields:
        if ((field['id'] == 29655218) or (field['id'] == 22917550) or (field['id'] == 43800168)):
            custom = custom+'\"'+str(field['value'])+'\", '
    data = data+'('+custom+'\"'+str(ticket.id)+'\", \"'+str(ticket.tags)+'\", \"'+str(ticket.group_id)+'\", '+'STR_TO_DATE(\''+str(ticket.created_at)+'\', \'%Y-%m-%dT%H:%i:%sZ\')'+', '+'STR_TO_DATE(\''+str(ticket.updated_at)+'\', \'%Y-%m-%dT%H:%i:%sZ\')),'+'\n'
    custom = ''
data = data[:-2]

# Writes end time of export to text file for use as start time of future export
with open("export_time.txt","w+") as f:
    f.write(str(result_generator.end_time))





