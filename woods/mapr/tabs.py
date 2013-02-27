from django.utils.translation import ugettext as _

from horizon import exceptions
from horizon import tabs

from . import utils
from .tables import InstancesTable


class DataTab(tabs.TableTab):
    name = _("Data")
    slug = "data"
    table_classes = (InstancesTable,)
    template_name = "horizon/common/_detail_table.html"
    preload = False

    def get_instances_data(self):
        try:
            instances = utils.get_instances_data(self.tab_group.request)
            #instances = utils.get_fake_instances_data(self.tab_group.request)
        except:
            instances = []
            exceptions.handle(self.tab_group.request,
                              _('Unable to retrieve instance list.'))
        return instances


class VizTab(tabs.Tab):
    name = _("Visualization")
    slug = "viz"
    template_name = "project/mapr/tabs.html"

    def get_context_data(self, request):
        return None


class Tabs(tabs.TabGroup):
    slug = "tabs"
    tabs = (VizTab, DataTab)
