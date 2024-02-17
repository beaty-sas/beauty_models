import os

from alembic.config import Config
from alembic import command

import beauty_models
from beauty_models.beauty_models import migrations


def migrate_db(sqlalchemy_database_uri: str):
    os.environ['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_database_uri
    companion_models_path = os.path.dirname(beauty_models.__path__[0])
    migrations_path = migrations.__path__[0]
    config_path = os.path.join(companion_models_path, 'beauty_models', 'alembic.ini')
    alembic_cfg = Config(config_path)
    alembic_cfg.set_main_option('script_location', migrations_path)
    command.upgrade(alembic_cfg, 'head')
