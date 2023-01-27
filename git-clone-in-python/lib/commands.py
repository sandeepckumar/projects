from gitrepo import repo_create

SUBCOMMANDS = {}


def register_func(name):
    def wrapper(func):
        SUBCOMMANDS.update({name: func})

    return wrapper


@register_func("add")
def cmd_add(args):
    pass


@register_func("cat-file")
def cmd_cat_file(args):
    pass


@register_func("checkout")
def cmd_checkout(args):
    pass


@register_func("hash-object")
def cmd_hash_object(args):
    pass


@register_func("init")
def cmd_init(args):
    repo_create(args.path)


@register_func("log")
def cmd_log(args):
    pass


@register_func("ls-files")
def cmd_ls_files(args):
    pass


@register_func("ls-tree")
def cmd_ls_tree(args):
    pass


@register_func("merge")
def cmd_merge(args):
    pass


@register_func("rebase")
def cmd_rebase(args):
    pass


@register_func("rev-parse")
def cmd_rev_parse(args):
    pass


@register_func("rm")
def cmd_rm(args):
    pass


@register_func("show-ref")
def cmd_show_ref(args):
    pass


@register_func("tag")
def cmd_tag(args):
    pass
