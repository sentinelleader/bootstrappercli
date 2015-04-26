#!/usr/bin/env python

from argparser import arg_parse 
from bootstrapcli import bootstrap, codeupdate, adhoc, adhocj, result

def main():
    args = arg_parse()

    if args['which'] == 'bootstrap':
        r_code,r_text =  bootstrap(args['host'], args['role'], args['env'])
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
    else:
        print "invalid command"
