from aws_cdk import core as cdk
from sso_stack import SsoPermissionSetStack
from config import SSOConfig

sso_config = SSOConfig(config_path='config/')

app = cdk.App()
SsoPermissionSetStack(app, "SsoPermissionSetStack", sso_config=sso_config)
app.synth()
