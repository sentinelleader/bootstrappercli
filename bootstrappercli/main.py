#!/usr/bin/env python

import sys
from argparser import arg_parse
from bootstrapcli import bootstrap, codeupdate, adhoc, adhocj, result, ec2list, launch_ec2, list_lc, create_lc
from slack_notify import post_hook
import pkg_resources
import subprocess

def main():
    user = (subprocess.check_output("whoami", shell=True)).rstrip()
    args = arg_parse()

    if args['which'] == 'launch-ec2':
        post_hook(user, args['which'], args['env'], args['role'])
        r_code,r_text = launch_ec2(args['instance_type'], args['role'], args['ip'], args['env'], args['public'])
        if r_code == 200:
            print "Job Queued Successfully. JobID %s" %r_text
        else:
            print "Failed to Queue to the Job. Please try again later"
    elif args['which'] == "list_lc":
        r_code,r_text =  list_lc(args['env'])
        print r_text
    elif args['which'] == "create_lc":
        r_code,r_text = create_lc(args['env'], args['instance_type'], args['role'], args['public'], args['ami'])
        if r_code == 200:
            print "Job Queued Successfully. JobID %s" %r_text
        else:
            print "Failed to Queue to the Job. Please try again later"
    elif args['which'] == 'bootstrap':
        post_hook(user, args['which'], args['env'], args['role'])
        r_code,r_text =  bootstrap(args['host'], args['role'], args['env'])
        if r_code == 200:
            print "Job Queued Successfully. JobID %s" %r_text
        else:
            print "Failed to Queue to the Job. Please try again later"
    elif args['which'] == 'codeupdate':
        post_hook(user, args['which'], args['env'], args['tag'])
        r_code,r_text = codeupdate(args['tag'], args['env'])
        if r_code == 200:
            print "Job Queued Successfully. JobID %s" %r_text
        else:
            print "Failed to Queue to the Job. Please try again later"
    elif args['which'] == 'adhoc':
        r_code,r_text = adhoc(args['host'], args['module'], args['args'], args['env'])
	print r_text
    elif args['which'] == 'adhocj':
        r_code,r_text = adhocj(args['host'], args['module'], args['args'], args['env'])
        if r_code == 200:
            print "Job Queued Successfully. JobID %s" %r_text
        else:
            print "Failed to Queue to the Job. Please try again later"
    elif args['which'] == 'result':
        r_code,r_text = result(args['jid'], args['env'])
	print r_text
    elif args['which'] == 'inventory':
        r_code,r_text = ec2list(args['pattern'], args['env'])
        print r_text
    elif args['which'] == 'version':
        bootstrapper_ver = pkg_resources.require("bootstrapper")[0].version
        print "Bootstrapper CLI version %s" %bootstrapper_ver
    else:
        print "invalid command"
