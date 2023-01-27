import os
from configparser import ConfigParser


def repo_path(repo, *path):
    return os.path.join(repo.gitdir, *path)


def repo_dir(repo, *path, mkdir=False):
    path = repo_path(repo, *path)
    if os.path.exists(path):
        if os.path.isdir(path):
            return path
        else:
            raise Exception("Not a directory {}".format(path))

    if mkdir:
        os.makedirs(path)
        return path
    else:
        return None


def repo_file(repo, *path, mkdir=False):
    if repo_dir(repo, *path[:-1], mkdir=mkdir):
        return repo_path(repo, *path)


def repo_default_config():
    # repositoryformatversion = 0: gitdir format.
    #                           0 means the initial format.
    #                           1 means same with extensions.
    #                           >1, git panic; this tool will only accept 0.
    # filemode = False: disable tracking of file mode changes in the work tree
    # bare = False: indicates that this repo has a worktree.
    conf = ConfigParser()
    conf.add_section("core")
    conf.set("core", "repositoryformatversion", "0")
    conf.set("core", "filemode", "false")
    conf.set("core", "bare", "false")
    return conf

