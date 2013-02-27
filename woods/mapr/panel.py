# -*- coding: utf-8 -*-
#
# import openstack_dashboard.dashboards.project.dashboard
# to register Mapr panel.
#
# ** HOW TO USE **
# # In settings.py
# HORIZON_CONFIG['customization_module'] = 'woods.mapr'
# INSTALLED_APPS += ('woods.mapr', )
#


from django.utils.translation import ugettext_lazy as _

from openstack_dashboard.dashboards.project import dashboard
import horizon


class Mapr(horizon.Panel):
    name = _("Mapr")
    slug = "mapr"

dashboard.Project.register(Mapr)
