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
module: network_device_functional_capability
short_description: Manage NetworkDeviceFunctionalCapability objects of Devices
description:
- Returns the functional-capability for given devices.
- Returns functional capability with given Id.
version_added: '1.0'
author: Rafael Campos (@racampos)
options:
  device_id:
    description:
    - Accepts comma separated deviceid's and return list of functional-capabilities for the given id's. If invalid or not-found id's are provided, null entry will be returned in the list.
    type: str
    required: True
  function_name:
    description:
    - FunctionName query parameter.
    type: str
  id:
    description:
    - Functional Capability UUID.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_functional_capability
# Reference by Internet resource
- name: NetworkDeviceFunctionalCapability reference
  description: Complete reference of the NetworkDeviceFunctionalCapability object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceFunctionalCapability reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_functional_capability_for_devices
  cisco.dnac.network_device_functional_capability:
    state: query  # required
    device_id: SomeValue  # string, required
    function_name: SomeValue  # string
  register: query_result
  
- name: get_functional_capability_by_id
  cisco.dnac.network_device_functional_capability:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result
  
"""

RETURN = """
get_functional_capability_for_devices:
    description: Returns the functional-capability for given devices.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        attributeInfo:
          description: It is the network device functional capability's attributeInfo.
          returned: always
          type: dict
        deviceId:
          description: It is the network device functional capability's deviceId.
          returned: always
          type: str
          sample: '<deviceid>'
        functionalCapability:
          description: It is the network device functional capability's functionalCapability.
          returned: always
          type: list
          contains:
            attributeInfo:
              description: It is the network device functional capability's attributeInfo.
              returned: always
              type: dict
            functionDetails:
              description: It is the network device functional capability's functionDetails.
              returned: always
              type: list
              contains:
                attributeInfo:
                  description: It is the network device functional capability's attributeInfo.
                  returned: always
                  type: dict
                id:
                  description: It is the network device functional capability's id.
                  returned: always
                  type: str
                  sample: '478012'
                propertyName:
                  description: It is the network device functional capability's propertyName.
                  returned: always
                  type: str
                  sample: '<propertyname>'
                stringValue:
                  description: It is the network device functional capability's stringValue.
                  returned: always
                  type: str
                  sample: '<stringvalue>'

            functionName:
              description: It is the network device functional capability's functionName.
              returned: always
              type: str
              sample: '<functionname>'
            functionOpState:
              description: It is the network device functional capability's functionOpState.
              returned: always
              type: str
              sample: '<functionopstate>'
            id:
              description: It is the network device functional capability's id.
              returned: always
              type: str
              sample: '478012'

        id:
          description: It is the network device functional capability's id.
          returned: always
          type: str
          sample: '478012'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_functional_capability_by_id:
    description: Returns functional capability with given Id.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        attributeInfo:
          description: It is the network device functional capability's attributeInfo.
          returned: always
          type: dict
        functionDetails:
          description: It is the network device functional capability's functionDetails.
          returned: always
          type: list
          contains:
            attributeInfo:
              description: It is the network device functional capability's attributeInfo.
              returned: always
              type: dict
            id:
              description: It is the network device functional capability's id.
              returned: always
              type: str
              sample: '478012'
            propertyName:
              description: It is the network device functional capability's propertyName.
              returned: always
              type: str
              sample: '<propertyname>'
            stringValue:
              description: It is the network device functional capability's stringValue.
              returned: always
              type: str
              sample: '<stringvalue>'

        functionName:
          description: It is the network device functional capability's functionName.
          returned: always
          type: str
          sample: '<functionname>'
        functionOpState:
          description: It is the network device functional capability's functionOpState.
          returned: always
          type: str
          sample: '<functionopstate>'
        id:
          description: It is the network device functional capability's id.
          returned: always
          type: str
          sample: '478012'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""
