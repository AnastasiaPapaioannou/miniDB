from database import Database
# create db with name "smdb"
db = Database('vsmdb', load=False)
# create a single table named "classroom"
db.create_table('classroom', ['building', 'room_number', 'capacity'], [str,str,int])
# db.create_table('class', ['build', 'room', 'cap'], [str,str,int])

# insert 5 rows
db.insert('classroom', ['Packard', '101', '500'])
db.insert('classroom', ['Painter', '514', '10'])
db.insert('classroom', ['Taylor', '3128', '70'])
# db.insert('class', ['Watson', '100', '30'])
# db.insert('class', ['Babe', '220', '80'])
db.update('classroom',300,'capacity','building==Packard')
# db.update('class',300,'capacity','building==Watson')
