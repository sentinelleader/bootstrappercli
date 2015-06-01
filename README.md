bootstrappercli
========

`boostrappercli` is a CLI that  talks to the Bootstrapper API and performs the Ansible tasks via the API.


####Supported Endpoints

  * launch-ec2 (Launches EC2 instances with/without EIP/Public IP)

  * Create/List ASG launch config's based on the Env

  * bootstrap (Bootstrapping the server via Ansible Playbook and Roles)

  * codeupdate (Performs Prod/Staging Code update via Ansible Playbook)

  * adhoc (Run's adhoc commands on the nodes)

  * result (Displays status of the Queued job in Bootstrapper)


####Installation

	$ python setup.py install

####CLI Options

	bootstrappercli -h
	usage: bootstrappercli [-h] {bootstrap,codeupdate,adhoc,adhocj,result} ...

	boostrappercli

	optional arguments:
	  -h, --help            show this help message and exit

	Endpoints:
	  Valid Endpoints

	  {bootstrap,codeupdate,adhoc,adhocj,result}
	                        additional help


  SubCommands

    * launch-ec2

        bootstrappercli launch-ec2 -h
        usage: bootstrappercli launch-ec2 [-h] -I INSTANCE_TYPE -r ROLE -i IP [-e ENV] -P
                                    PUBLIC

        optional arguments:
          -h, --help            show this help message and exit
          -I INSTANCE_TYPE, --instance_type INSTANCE_TYPE
                                EC2 Instance Type
          -r ROLE, --role ROLE  Role EC2 Tag Value
          -i IP, --ip IP        Last Two Octects of the Private IP
          -e ENV, --env ENV     Inventory ENV
          -P PUBLIC, --public PUBLIC
                                Public IP for instance, values are True/False

    * bootstrap

	bootstrappercli bootstrap -h
	usage: bootstrappercli bootstrap [-h] -r ROLE -H HOST

	optional arguments:
	  -h, --help            show this help message and exit
	  -r ROLE, --role ROLE  Ansible Roles
	  -H HOST, --host HOST  Host info (fqdn, ip, pattern)
	  -e ENV, --env ENV     Inventory ENV

    * codeupdate

	bootstrappercli codeupdate -h
	usage: bootstrappercli codeupdate [-h] -t TAG

	optional arguments:
	  -h, --help         show this help message and exit
	  -t TAG, --tag TAG  Ansible playbook Tag
	  -e ENV, --env ENV     Inventory ENV

    * adhoc

	bootstrappercli adhoc -h
	usage: bootstrappercli adhoc [-h] -H HOST -m MODULE [-a ARGS] [-e ENV]

	optional arguments:
	  -h, --help            show this help message and exit
	  -H HOST, --host HOST  Host info (fqdn, ip, pattern)
	  -m MODULE, --module MODULE
	                        Ansible Module
	  -a ARGS, --args ARGS  Ansible Module Args
	  -e ENV, --env ENV     Inventory ENV

    * inventory

	bootstrappercli inventory -h
	usage: bootstrappercli inventory [-h] -p PATTERN [-e ENV]

	optional arguments:
	  -h, --help            show this help message and exit
	  -p PATTERN, --pattern PATTERN
	                        Inventory Search Pattern
	  -e ENV, --env ENV     Inventory ENV

    * result

	bootstrappercli result -h
	usage: bootstrappercli result [-h] -j JID

	optional arguments:
	  -h, --help         show this help message and exit
	  -j JID, --jid JID  Job ID


#### Sample Output

	$ bootstrappercli.py adhocj -H tag_Role_vpmtr -m ping -e dev
	  a559263b-ced6-468d-9b00-eb96257f4ed9

	$ bootstrappercli.py result -j a559263b-ced6-468d-9b00-eb96257f4ed9 -e dev
	  {"dark": {}, "contacted": {"172.20.1.210": {"invocation": {"module_name": "ping", "module_args": ""}, "changed": false, "ping": "pong"}}}

   EC2-Launch:

        ➜  ~  bootstrappercli launch-ec2 -I t2.micro -r test -i 1.249 -e dev -P True
              Job Queued Successfully. JobID bbff212b-a267-4380-b6c6-58322e89549b

        ➜  ~  bootstrappercli result -j bbff212b-a267-4380-b6c6-58322e89549b

        ➜  ~ bootstrappercli inventory -p tag_Role_test -e dev
             ["172.20.1.249"]

    Note: Currently bootstrappercli doesnt support Security Group creation, so a valid security group must exists for the role in the Name format `sg_vpc_<role>`

