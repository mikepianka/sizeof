from cli import run_cli
from sizeof import run


config_dict = run_cli()

run(
    root_dir=config_dict["root_dir"],
    create_log=config_dict["create_log"],
    by_subdir=config_dict["by_subdir"],
)
