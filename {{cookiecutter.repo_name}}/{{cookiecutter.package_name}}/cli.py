from argparse import ArgumentParser
from {{ cookiecutter['package_name'] }} import __version__

def subcommand1(args):
    print('Do something with subcommand 1', args)

def cli(args=None):
    p = ArgumentParser(
        description="{{ cookiecutter['project_short_description']}}",
        conflict_handler='resolve'
    )
    p.set_defaults(func=lambda args: p.print_help())
    p.add_argument(
        '-V', '--version',
        action='version',
        help='Show the conda-prefix-replacement version number and exit.',
        version="{{ cookiecutter['package_name']}} %s" % __version__,
    )

    args, unknown = p.parse_known_args(args)

    # do something with the sub commands
    sub_p = p.add_subparsers(help='sub-command help')
    # add show all sensors command
    subcmd1 = sub_p.add_parser('sub1', help='subcommand 1')
    subcmd1.add_argument('--input-file', type=str, required=False, help='an input file argument')
    subcmd1.set_defaults(func=subcommand1)

    # Now call the appropriate response.
    pargs = p.parse_args(args)
    pargs.func(pargs)
    return 
    # No return value means no error.
    # Return a value of 1 or higher to signify an error.
    # See https://docs.python.org/3/library/sys.html#sys.exit


if __name__ == '__main__':
    import sys
    cli(sys.argv[1:])
