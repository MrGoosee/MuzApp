import peewee as pw

db = pw.SqliteDatabase('db.sqlite3')


class DefaultDBMeta(pw.Model):
    class Meta:
        database = db


class MapCoordinates(DefaultDBMeta):
    longitude = pw.TextField() # Долгота
    latitude = pw.TextField() # Широтка


class Museum(DefaultDBMeta):
    title = pw.CharField(max_length=100)
    description = pw.TextField()
    image = pw.CharField()
    contacts = pw.TextField()
    website = pw.TextField()
    address = pw.TextField()
    coordinates_id = pw.ForeignKeyField(MapCoordinates, backref='museum')
    work_time = pw.TextField()


class Events(DefaultDBMeta):
    title = pw.CharField(max_length=1000)
    description = pw.TextField()
    image = pw.CharField()
    address = pw.TextField()
    museum = pw.ForeignKeyField(Museum, backref='events')

