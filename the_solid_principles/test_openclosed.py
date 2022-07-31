# from openclosed_3 import SystemMonitor
from lsp_2 import SystemMonitor

l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
l4 = SystemMonitor({"before": {}, "after": {"transaction": "Tx001"}})


print('l1: ', l1.identify_event().__class__.__name__)
print('l2: ', l2.identify_event().__class__.__name__)
print('l3: ', l3.identify_event().__class__.__name__)
print('l4: ', l4.identify_event().__class__.__name__)