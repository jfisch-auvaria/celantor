from aws_cdk import (
    core as cdk,
    aws_sso as sso,
)
from config import SSOConfig

class SsoPermissionSetStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, sso_config: SSOConfig, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # CDK to create the Permission Sets
        # Create and Assign Permission set for each configuration
        for set_config in sso_config.get_permission_sets():
            name = set_config['name']
            description = set_config['description']
            session_duration = set_config['session_duration']
            accounts = set_config['accounts']
            groups = set_config['groups']
            managed_policies = set_config['managed_policies']
            inline_policy = set_config['inline_policy']

            # Create the Permission Set
            permission_set = sso.CfnPermissionSet(self, f"{name}_Set",
                                                  instance_arn=sso_config.get_sso_config()['sso_instance_arn'],
                                                  name=name,
                                                  description=description,
                                                  session_duration=str(session_duration),
                                                  inline_policy=inline_policy,
                                                  managed_policies=managed_policies)

            # Assign to Accounts and Groups
            for acc in accounts:
                acc_num = sso_config.get_account_list()[acc]
                for group in groups:
                    group_id = sso_config.get_group_list()[group]
                    sso.CfnAssignment(self, f"{name}_{acc_num}_{group}_Assignment",
                                      instance_arn=sso_config.get_sso_config()['sso_instance_arn'],
                                      permission_set_arn=permission_set.attr_permission_set_arn,
                                      principal_id=group_id,
                                      principal_type='GROUP',
                                      target_id=acc_num,
                                      target_type='AWS_ACCOUNT')
