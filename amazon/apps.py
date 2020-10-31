from django.apps import AppConfig
#from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.utils.translation import ugettext_lazy as _

class AmazonConfig(AppConfig):
    name = 'amazon'
   #verbose_name = _('amazons')



def ready(self):
        import amazon.signals
       #import cmdbox.amazon.signals  # noqa
       #post_save.connect(create_user_profile, sender=User)
       #post_save.connect(save_user_profile, sender=User)