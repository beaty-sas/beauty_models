import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine

from beauty_models.models import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

IGNORE_TABLES = [
    'geocode_settings',
    'zip_lookup',
    'zip_state_loc',
    'addrfeat',
    'zip_lookup_base',
    'street_type_lookup',
    'loader_platform',
    'state_lookup',
    'countysub_lookup',
    'county_lookup',
    'bg',
    'addr',
    'state',
    'tract',
    'topology',
    'cousub',
    'tabblock20',
    'loader_lookuptables',
    'secondary_unit_lookup',
    'pagc_lex',
    'loader_variables',
    'pagc_gaz',
    'featnames',
    'tabblock',
    'faces',
    'layer',
    'pagc_rules',
    'place',
    'pagc_rules',
    'zip_lookup_all',
    'zcta5',
    'geocode_settings_default',
    'county',
    'place_lookup',
    'direction_lookup',
    'zip_state',
    'spatial_ref_sys',
    'edges',
]


def include_object(object, name, type_, reflected, compare_to):
    if type_ == 'table' and (name in IGNORE_TABLES or object.info.get('skip_autogenerate', False)):
        return False

    return True


def get_url():
    url = os.environ.get('SQLALCHEMY_DATABASE_URI')
    if not url:
        raise ValueError('"SQLALCHEMY_DATABASE_URI" env variable should be specified')
    return url


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={'paramstyle': 'named'},
        include_object=include_object,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(get_url())

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
