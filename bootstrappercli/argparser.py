import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Bootstrapper Cli')
    subparsers = parser.add_subparsers(
        title='Endpoints', description='Valid Endpoints',
        help='additional help')
    parser_bstap = subparsers.add_parser('bootstrap')
    parser_bstap.set_defaults(which='bootstrap')
    parser_bstap.add_argument(
        '-r', '--role', required=True, help='Ansible Roles')
    parser_bstap.add_argument(
        '-H', '--host', required=True, help='Host info (fqdn, ip, pattern)')
    parser_bstap.add_argument(
        '-e', '--env', default='dev', help='Inventory ENV')

    parser_cupdate = subparsers.add_parser('codeupdate')
    parser_cupdate.set_defaults(which='codeupdate')
    parser_cupdate.add_argument(
        '-t', '--tag', required=True, help='Ansible playbook Tag')
    parser_cupdate.add_argument(
        '-e', '--env', default='dev', help='Inventory ENV')

    parser_adhoc = subparsers.add_parser('adhoc')
    parser_adhoc.set_defaults(which='adhoc')
    parser_adhoc.add_argument(
        '-H', '--host', required=True, help='Host info (fqdn, ip, pattern)')
    parser_adhoc.add_argument(
        '-m', '--module', required=True, help='Ansible Module')
    parser_adhoc.add_argument(
        '-a', '--args', help='Ansible Module Args')
    parser_adhoc.add_argument(
        '-e', '--env', default='dev', help='Inventory ENV')

    parser_adhocj = subparsers.add_parser('adhocj')
    parser_adhocj.set_defaults(which='adhocj')
    parser_adhocj.add_argument(
        '-H', '--host', required=True, help='Host info (fqdn, ip, pattern)')
    parser_adhocj.add_argument(
        '-m', '--module', required=True, help='Ansible Module')
    parser_adhocj.add_argument(
        '-a', '--args', help='Ansible Module Args')
    parser_adhocj.add_argument(
        '-e', '--env', default='dev', help='Inventory ENV')

    parser_result = subparsers.add_parser('result')
    parser_result.set_defaults(which='result')
    parser_result.add_argument(
        '-j', '--jid', required=True, help='Job ID')
    parser_result.add_argument(
        '-e', '--env', default='dev', help='Inventory ENV')

    args = vars(parser.parse_args())
    return args
