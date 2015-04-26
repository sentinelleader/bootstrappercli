BootstrapCLI
============

`BootstrapCLI` is a CLI tool for [bootstrapper](https://github.com/sentinelleader/bootstrapper) project. It talks to the Bootstrapper API and performs the actions via the API.

####Supported Endpoints

  * bootstrap (Bootstrapping the server via Ansible Playbook and Roles)   

  * adhoc/adhocj (Run's adhoc commands on the nodes)

  * result (Displays status of the Queued job in Bootstrapper)

	
####Instalaltion

	$ python setup.py install

####CLI Options

	bootstrappercli -h
	usage: bootstrappercli [-h] {bootstrap,codeupdate,adhoc,adhocj,result} ...
	
	BootstrapCLI
	
	optional arguments:
	  -h, --help            show this help message and exit
	
	Endpoints:
	  Valid Endpoints
	
	  {bootstrap,codeupdate,adhoc,adhocj,result}
	                        additional help


  SubCommands

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

    * result

	bootstrappercli result -h
	usage: bootstrappercli result [-h] -j JID
	
	optional arguments:
	  -h, --help         show this help message and exit
	  -j JID, --jid JID  Job ID


#### Sample Output

	$ bootstrappercli.py adhocj -H tag_Role_mysqlmaster -m ping -e dev
	  a559263b-ced6-468d-9b00-eb96257f4ed9

	$ bootstrappercli.py result -j a559263b-ced6-468d-9b00-eb96257f4ed9 -e dev
	  {"dark": {}, "contacted": {"172.20.1.210": {"invocation": {"module_name": "ping", "module_args": ""}, "changed": false, "ping": "pong"}}}


####ToDo

  * AWS management via Bootstrapper API (Machine launch, DNS entry, ec2_tags, ec2_volumes)

