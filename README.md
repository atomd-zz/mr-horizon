woods
=====

##setup

```
from openstack_dashboard.settings import INSTALLED_APPS, HORIZON_CONFIG

HORIZON_CONFIG['customization_module'] = 'woods.mapr'
INSTALLED_APPS += ('woods.mapr', )
```
