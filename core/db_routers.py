from decouple import config

class TesteAppRouter:
    """Roteador para controlar as operações com o banco de dados dos modelos do app 'teste_app'."""
    def db_for_read(self, model, **hints):
        if model._meta.app_label == f'{config("DB_SCHEMA_TEST_APP")}':
            return f'{config("DB_SCHEMA_TEST_APP")}'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == f'{config("DB_SCHEMA_TEST_APP")}':
            return f'{config("DB_SCHEMA_TEST_APP")}'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == f'{config("DB_SCHEMA_TEST_APP")}' or \
           obj2._meta.app_label == f'{config("DB_SCHEMA_TEST_APP")}':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == f'{config("DB_SCHEMA_TEST_APP")}':
            return db == 'default'
        return None

class TesteAppOutroRouter:
    """Roteador para controlar as operações com o banco de dados dos modelos do app 'teste_app_outro'."""
    def db_for_read(self, model, **hints):
        if model._meta.app_label == f'{config("DB_SCHEMA_TEST_APP_OUTRO")}':
            return f'{config("DB_SCHEMA_TEST_APP_OUTRO")}'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == f'{config("DB_SCHEMA_TEST_APP_OUTRO")}':
            return f'{config("DB_SCHEMA_TEST_APP_OUTRO")}'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == f'{config("DB_SCHEMA_TEST_APP_OUTRO")}' or \
           obj2._meta.app_label == f'{config("DB_SCHEMA_TEST_APP_OUTRO")}':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == f'{config("DB_SCHEMA_TEST_APP_OUTRO")}':
            return db == 'default'
        return None
