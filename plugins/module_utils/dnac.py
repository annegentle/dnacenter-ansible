#!/usr/bin/env python

import json

# The following import uses a local code for testing purposes
from dnacentersdk import api


ERR_WRONG_METHOD = "Wrong method '{}'"
ERR_STATE_NOT_SUPPORTED = "State '{}' not supported by this module"
ERR_UNKNOWN = "Unknown error. More than one operation matched the given arguments"
ERR_NO_MATCHING_OPERATION = "There are no matching operations for the given arguments"

def msg(message, arg=""):
    return message.format(arg)

def dnac_argument_spec():
    return dict(
        host=dict(type='str', required=True, aliases=['hostname']),
        port=dict(type='int', required=False, default=443),
        username=dict(type='str', default='admin', aliases=['user']),
        password=dict(type='str', no_log=True),
        verify=dict(type='bool', default=True),
        version=dict(type='str', default="2.1.1"),
        state=dict(type='str', default='present', choices=['absent', 'present', 'query']),
        #use_proxy=dict(type='bool', default=True),
        #use_ssl=dict(type='bool', default=True),
        #validate_certs=dict(type='bool', default=True),
    )


class Parameter(object):

    def __init__(self, param):
        self.__dict__ = param

    def _get_type(self):
        if self.type == "string":
            return "str"
        elif self.type == "boolean":
            return "bool"
        elif self.type == "integer":
            return "int"
        elif self.type == "array":
            return "list"
        elif self.type == "any":
            return "raw"

    def is_required(self):
        _required = False
        if "required" in self.__dict__.keys():
            _required = self.required
        return _required

    def _is_enum(self):
        return "enum" in self.__dict__.keys()

    def _get_choices(self):
        return list(map(str.lower, self.enum))

    def _has_default(self):
        return "default" in self.__dict__.keys()

    def get_dict(self):
        outer_dict = dict()
        inner_dict = dict()
        inner_dict["type"] = self._get_type()
        inner_dict["required"] = self.is_required()
        if self._is_enum():
            inner_dict["choices"] = self._get_choices()
        if self._has_default():
            inner_dict["default"] = self.default
        outer_dict[self.name] = inner_dict
        return outer_dict


class Function(object):

    def __init__(self, name, params):
        self.name = name
        self.params = []
        for param in params:
            new_param = Parameter(param)
            self.params.append(new_param)

    def get_required_params(self, object=False):
        required_params = []
        for param in self.params:
            if param.is_required():
                if object:
                    required_params.append(param)
                else:
                    required_params.append(param.name)
        return required_params

    # Returns true if all the params required by this function are 
    # present in the module_params passed to the Ansible module
    def has_required_params(self, module_params):
        return set(self.get_required_params()).issubset(module_params.keys())

    # Returns true if all the module_params passed to the Ansible module
    # are present in the list of required params for this function
    def needs_passed_params(self, module_params):
        return set(module_params.keys()).issubset(self.get_required_params())




class ModuleDefinition(object):

    def __init__(self, module_name):
        with open("./module_definitions/{}.json".format(module_name)) as json_file:
            data = json.load(json_file)
            self.name = data["name"]
            self.family = data["family"]
            _params = data["parameters"]
            _operations = data["operations"]
            json_file.close()

        self.methods = ["post", "put", "delete", "get"]

        self.operations = dict.fromkeys(self.methods, [])
        for method, func_list in _operations.items():
            func_obj_list = []
            for func_name in func_list:
                function = Function(func_name, _params[func_name])
                func_obj_list.append(function)
            self.operations[method] = func_obj_list
        
        self.state = dict(zip(self.methods, ["present", "present", "absent", "query"]))

        self.common_params = ["username",
                              "password",
                              "host",
                              "port",
                              "version",
                              "verify",
                              "state"
                              ]
        
    # Strips the common module parameters from the passed parameters
    def _strip_common_params(self, module_params):
        return { k: v for k, v in module_params.items() if k not in self.common_params }

    # Strips all unused parameters (those that were not explicitly passed by the user)
    def _strip_unused_params(self, module_params):
        return { k: v for k, v in module_params.items() if v }

    # Retrieves all the functions supported by this module
    def get_functions(self):
        functions = []
        for func_list in self.operations.values():
            for function in func_list:
                functions.append(function)
        return functions


    # Retrieves a list with the parameters that are required
    # by all the functions supported by this module
    def _get_common_required_params(self):
        functions = self.get_functions()
        common_required_params = functions[0].get_required_params()
        for i in range(1, len(functions)):
            # Gets the intersection of two lists
            common_required_params = \
                    [item for item in common_required_params if item in functions[i].get_required_params()]
        return common_required_params


    # Retrieves a dictionary with all the parameters supported by this module
    # This dictionary is later used to instantiate the AnsibleModule class
    def get_argument_spec_dict(self):
        param_dict = dict()
        for function in self.get_functions():
            for param in function.params:    
                param_dict.update(param.get_dict())
        
        # If a parameter is required by all functions in a module
        # then it's a required parameter of the module
        for param, attr in param_dict.items():
            attr["required"] = param in self._get_common_required_params()

        return param_dict


    # Retrieves the function that exactly matches the given method and module parameters.
    def get_function(self, method, module_params):
        module_params = self._strip_common_params(module_params)
        module_params = self._strip_unused_params(module_params)
        if method in self.methods:
            ops = self.operations[method]
        else:
            message = msg(ERR_WRONG_METHOD, method) # Wrong method '{}'
            return None, message

        if len(ops) == 0:
            message = msg(ERR_STATE_NOT_SUPPORTED, self.state[method]) # State '{}' not supported by this module
            return None, message
        
        valid_ops = []
        for function in ops:
            if function.has_required_params(module_params) and function.needs_passed_params(module_params):
                valid_ops.append(function)

        if len(valid_ops) == 0:
            message = msg(ERR_NO_MATCHING_OPERATION) # "There are no matching operations for the given arguments"
            return None, message
        
        elif len(valid_ops) == 1:
            function = valid_ops[0] 
            return function, "Success"

        else:
            message = msg(ERR_UNKNOWN) # Unknown error. More than one operation matched the given arguments.
            return None, message
            
        

# Troubleshooting code

        # out = ""
        # for name, value in module_params.items():
        #     out = out + " {} ".format(value)
        # raise Exception(out)


class DNACModule(object):

    def __init__(self, module):
        self.module = module
        self.params = module.params
        self.response = None
        self.result = dict(changed=False)
        self.error = dict(code=None, text=None)
        self.dnac = api.DNACenterAPI(username=self.params['username'],
                        password=self.params['password'],
                        base_url="https://{}:{}".format(self.params['host'], self.params['port']),
                        version=self.params['version'],
                        verify=self.params['verify'])
        

       
        
    def exec(self, function, family):
        params = { param.name : self.params[param.name] for param in function.get_required_params(object=True)}
        family = getattr(self.dnac, family)
        func = getattr(family, function.name)
        return func(**params)


        



def main():
    pass


if __name__ == '__main__':
    main()