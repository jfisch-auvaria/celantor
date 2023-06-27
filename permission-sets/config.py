import json
import os

class SSOConfig:
    def __init__(self, config_path):
        with open(config_path + '/sso_config.json', 'r') as f:
            self.sso_config = json.load(f)

        with open(config_path + '/accounts.json', 'r') as f:
            self.account_list = json.load(f)

        with open(config_path + '/groups.json', 'r') as f:
            self.group_list = json.load(f)

        # Load the permission set configurations
        self.permission_sets = []
        permission_set_dir =  './permission_sets'
        for filename in os.listdir(permission_set_dir):
            if filename.endswith('.json'):
                with open(os.path.join(permission_set_dir, filename)) as f:
                    self.permission_sets.append(json.load(f))

    def get_sso_config(self):
        return self.sso_config

    def get_account_list(self):
        return self.account_list

    def get_group_list(self):
        return self.group_list

    def get_permission_sets(self):
        return self.permission_sets
