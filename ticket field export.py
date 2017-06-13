import zenpy, datetime, zdcreds

zenpy_client = zenpy.Zenpy(**zdcreds.creds)

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
result_generator = zenpy_client.tickets.incremental(start_time=yesterday)

row = ''
for ticket in result_generator:
    for field in ticket.custom_fields:
        if ((field['id'] == 29655218) or (field['id'] == 22917550) or (field['id'] == 43800168)):
            row = row+'\''+str(field['value'])+'\', '
    print(row+'\''+str(ticket.id)+'\', \''+str(ticket.tags)+'\', \''+str(ticket.group_id)+'\', \''+str(ticket.created_at)+'\', \''+str(ticket.updated_at)+'\'')
    row = ''

# Output columns are ordered as follows: platform, player_id, location, ticket_id, ticket_tags, group, ticket_created, last_update
