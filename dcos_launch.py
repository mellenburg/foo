def aws_super_duper_call():
    raise Exception("YOU HAVENT AUTHENTICATED")


def create(arg_list):
    aws_super_duper_call()
    return 0


def describe(arg_list):
    return 0


class DcosCluster:
    def __init__(self, config):
        self.config


def get_dcos_from_config(config):
    assert isinstance(config, dict)
    return
