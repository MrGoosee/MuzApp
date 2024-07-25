from playhouse.migrate import *
from models import *
my_db = SqliteDatabase('db.sqlite3')
migrator = SqliteMigrator(my_db)

coordinates_id = pw.ForeignKeyField(MapCoordinates, backref='museum')

migrate(
    migrator.add_column('museum', 'coordinates_id', coordinates_id),
)