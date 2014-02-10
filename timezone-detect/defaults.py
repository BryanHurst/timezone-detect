from django.conf import settings

# These countries will be prioritised in the search
# for a matching timezone.
# Defaults to top Internet using countries.
TZ_DETECT_COUNTRIES = getattr(settings, 'TZ_DETECT_COUNTRIES', ('US', 'CN', 'IN', 'JP', 'BR', 'RU', 'DE', 'FR', 'GB'))