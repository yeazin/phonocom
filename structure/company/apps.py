from django.apps import AppConfig


class CompanyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'structure.company'

    def ready(self):
        import structure.company.signals.phone_signals
        import structure.company.signals.track_signals