from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.project import dashboard


class Mapr(horizon.Panel):
    name = _("Mapr")
    slug = "mapr"


dashboard.Project.register(Mapr)
