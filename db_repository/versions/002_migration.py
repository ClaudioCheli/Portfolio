from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
image = Table('image', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('project', Integer),
    Column('imagePath', String(length=100)),
)

project = Table('project', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=40)),
    Column('imagePath', VARCHAR(length=100)),
)

project = Table('project', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=40)),
    Column('shortDescription', String(length=100)),
    Column('description', String(length=100)),
    Column('mainImage', String(length=100)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['image'].create()
    pre_meta.tables['project'].columns['imagePath'].drop()
    post_meta.tables['project'].columns['description'].create()
    post_meta.tables['project'].columns['mainImage'].create()
    post_meta.tables['project'].columns['shortDescription'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['image'].drop()
    pre_meta.tables['project'].columns['imagePath'].create()
    post_meta.tables['project'].columns['description'].drop()
    post_meta.tables['project'].columns['mainImage'].drop()
    post_meta.tables['project'].columns['shortDescription'].drop()
