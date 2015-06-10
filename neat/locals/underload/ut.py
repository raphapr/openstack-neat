from contracts import contract
from neat.contracts_primitive import *
from neat.contracts_extra import *

import logging
log = logging.getLogger(__name__)

"""

UT algorithm, a algorithm that considers memory and CPU of hosts [1]

[1]  A. Horri, A. Rahmaniana and GH. Dastghaibyfard, "Energy and Performance-aware Virtual Machine Consolidation in Cloud Computing A Two Dimensional Approach"

"""

@contract
def compute_ut(vms_cpu, vms_ram):
    """
        :param vms_cpu: A map of VM UUID and their CPU utilization histories.
         :type vms_cpu: dict(str: list)

        :param vms_ram: A map of VM UUID and their RAM usage data.
         :type vms_ram: dict(str: number)

        :return: A VM UUID to migrate (candidate)
         :rtype: str
    """

    vm_candidate= None 
    last_vm = None
    ut = {} # dict
    alpha = 0.6 # the weight, where 0 < alpha < 1
    for vm, cpu in vms_cpu.items():
        ut[vm] = (alpha*vms_cpu[vm]) + ((1-alpha)*vms_ram[vm])
        if ut.has_key(last_vm) == False:
            last_vm = vm
            continue
        if ut[vm] < ut[last_vm]:
            vm_candidate = vm
        last_vm = vm
    return vm_candidate
