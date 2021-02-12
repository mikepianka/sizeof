import os
import math


def prettify_bytes(bytes):
    if bytes == 0:
        return "0B"

    size_names = ["B", "KB", "MB", "GB", "TB"]

    i = int(math.floor(math.log(bytes, 1024)))
    p = math.pow(1024, i)
    s = round(bytes / p, 2)

    return f"{s} {size_names[i]}"


def write_size_log(msg, log_dir):
    log_path = log_dir + os.sep + "sizelog.txt"

    with open(log_path, "w") as size_log:
        size_log.write(msg)

    print(f"Created {log_path}")


def get_size(start_dir, log):
    total_size = 0
    files = 0
    print(f"Calculating total size of {start_dir}...")

    for dirpath, dirnames, filenames in os.walk(start_dir):
        for f in filenames:
            filepath = os.path.join(dirpath, f)
            # skip if it is a symbolic link
            if not os.path.islink(filepath):
                total_size += os.path.getsize(filepath)
                files += 1

    total_size_pretty = prettify_bytes(total_size)
    msg = f"Finished! {files:,} files containing {total_size_pretty} in {start_dir}"

    if log:
        write_size_log(msg, start_dir)

    print(msg)
    return total_size


def run(root_dir, create_log=True, by_subdir=False):
    if not by_subdir:
        get_size(start_dir=root_dir, log=create_log)
    else:
        contents = os.listdir(root_dir)
        for item in contents:
            item_path = root_dir + os.sep + item
            if os.path.isdir(item_path):
                get_size(start_dir=item_path, log=create_log)
