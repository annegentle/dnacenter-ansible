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
module: sda_auth_profile
short_description: Manage SdaAuthProfile objects of Sda
description:
- Add default authentication profile in SDA Fabric.
- Get default authentication profile from SDA Fabric.
- Add default authentication profile in SDA Fabric.
- Update default authentication profile in SDA Fabric.
version_added: '1.0'
author: Rafael Campos (@racampos)
options:
  site_name_hierarchy:
    description:
    - SiteNameHierarchy query parameter.
    type: str
    required: True
  payload:
    description:
    - An object to send in the Request body.
    type: list
    required: True
    elements: dict
    suboptions:
      authenticateTemplateName:
        description:
        - It is the sda auth profile's authenticateTemplateName.
        type: str
      siteNameHierarchy:
        description:
        - It is the sda auth profile's siteNameHierarchy.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_auth_profile
# Reference by Internet resource
- name: SdaAuthProfile reference
  description: Complete reference of the SdaAuthProfile object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaAuthProfile reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: delete_default_authentication_profile
  cisco.dnac.sda_auth_profile:
    state: delete  # required
    site_name_hierarchy: SomeValue  # string, required
  
- name: get_default_authentication_profile
  cisco.dnac.sda_auth_profile:
    state: query  # required
    site_name_hierarchy: SomeValue  # string, required
  register: query_result
  
- name: add_default_authentication_profile
  cisco.dnac.sda_auth_profile:
    state: create  # required
    payload:  # required
    - siteNameHierarchy: SomeValue  # string
      authenticateTemplateName: SomeValue  # string
  
- name: update_default_authentication_profile
  cisco.dnac.sda_auth_profile:
    state: update  # required
    payload:  # required
    - siteNameHierarchy: SomeValue  # string
      authenticateTemplateName: SomeValue  # string
  
"""

RETURN = """
delete_default_authentication_profile:
    description: Add default authentication profile in SDA Fabric.
    returned: success
    type: dict
    contains:
    status:
      description: Status, property of the response body.
      returned: success
      type: str
      sample: '<status>'
    description:
      description: Description, property of the response body.
      returned: success
      type: str
      sample: '<description>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'

get_default_authentication_profile:
    description: Get default authentication profile from SDA Fabric.
    returned: always
    type: dict
    contains:
    siteNameHierarchy:
      description: Site Name Hierarchy, property of the response body.
      returned: always
      type: str
      sample: '<sitenamehierarchy>'
    authenticateTemplateName:
      description: Authenticate Template Name, property of the response body.
      returned: always
      type: str
      sample: '<authenticatetemplatename>'
    authenticateTemplateId:
      description: Authenticate Template Id, property of the response body.
      returned: always
      type: str
      sample: '<authenticatetemplateid>'

add_default_authentication_profile:
    description: Add default authentication profile in SDA Fabric.
    returned: success
    type: dict
    contains:
    status:
      description: Status, property of the response body.
      returned: success
      type: str
      sample: '<status>'
    description:
      description: Description, property of the response body.
      returned: success
      type: str
      sample: '<description>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'

update_default_authentication_profile:
    description: Update default authentication profile in SDA Fabric.
    returned: changed
    type: dict
    contains:
    status:
      description: Status, property of the response body.
      returned: changed
      type: str
      sample: '<status>'
    description:
      description: Description, property of the response body.
      returned: changed
      type: str
      sample: '<description>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: changed
      type: str
      sample: '<executionstatusurl>'

"""
