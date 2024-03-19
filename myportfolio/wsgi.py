from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'media'))
application.add_files(os.path.join(BASE_DIR, 'media'), prefix='media/')