from cli import run_cli
from sizeof import get_size


config_dict = run_cli()

get_size(root_dir=config_dict["root_dir"], create_log=config_dict["create_log"])
