#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: site_device
short_description: Manage SiteDevice objects of Sites
description:
- Assigns list of devices to a site.
version_added: '1.0'
author: Rafael Campos (@racampos)
options:
  site_id:
    description:
    - Site id to which site the device to assign.
    type: str
    required: True
  device:
    description:
    - Device, property of the request body (list of objects).
    type: list
    required: True
    elements: dict
    suboptions:
      ip:
        description:
        - It is the site device's ip.
        type: str
        required: True


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.site_device
# Reference by Internet resource
- name: SiteDevice reference
  description: Complete reference of the SiteDevice object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SiteDevice reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: assign_device_to_site
  cisco.dnac.site_device:
    state: create  # required
    site_id: SomeValue  # string, required
    device:  # required
    - ip: SomeValue  # string, required
  
"""

RETURN = """
assign_device_to_site:
    description: Assigns list of devices to a site.
    returned: success
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

"""
