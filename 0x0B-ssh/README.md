0x0B. SSH
 - DevOps
 - SSH
 - Network
 - SysAdmin
 - Security

#### What is a server?
	- A server is a computer system or program that provides resources, services or data to other computers or devices on a network. 

#### Where servers usually live?
	- Servers can live in a variety of locations depending on the specific needs of the user or organization. Some of the common places where servers live include data centers, on-premises (some organizations choose to host their servers on their premises), in the cloud. 

#### What is SSH?
	- SSH stands for Secure Shell. It is a secure network protocol used to establish a secure and encrypted connection between two computers.

#### How to create an SSH RSA key pair?
	- On linux, you use the `ssh-keygen` utility.
		- open a terminal window and type ssh-keygen -t rsa

#### How to connect to a remote host using an SSH RSA key pair?
	- Generate an RSA key pair with the public key copied to the remote host

	- connect to remote host using SSH

#### The advantage of using #!/usr/bin/env bash instead of /bin/bash?
	- The advantage of using #!/usr/bin/env bash instead of #!/bin/bash in a bash script is that it allows the script to use the user's preferred shell environment instead of a hardcoded path to the Bash shell executable
