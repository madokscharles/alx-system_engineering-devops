0x0B. SSH
- DevOps - SSH - Network - SysAdmin - Security

# Server and SSH Basics

This repository provides a brief introduction to servers, SSH, and using SSH RSA key pairs. It also highlights the advantages of using `#!/usr/bin/env bash` instead of `/bin/bash`.

## What is a server?

A server is a computer or system that provides services or resources to other computers, known as clients, over a network. It is designed to handle requests and deliver data or perform tasks for connected clients.

## Where do servers usually live?

Servers can be located in data centers or hosted remotely in the cloud. They are often housed in dedicated facilities with redundant power supplies, cooling systems, and robust network connections.

## What is SSH?

SSH (Secure Shell) is a network protocol that enables secure communication between a client and a remote server. It provides a secure way to log into and manage a remote machine over an unsecured network.

## How to create an SSH RSA key pair?

To create an SSH RSA key pair, follow these steps:

1. Open a terminal or command prompt.
2. Type the following command: `ssh-keygen -t rsa`.
3. You will be prompted to enter a file location to save the key pair and to set a passphrase (optional).
4. Press Enter to accept the default file location or provide a custom one.
5. Your SSH RSA key pair will be generated and saved.

## How to connect to a remote host using an SSH RSA key pair?

To connect to a remote host using an SSH RSA key pair, use the following steps:

1. Obtain the public key of the remote host.
2. Open a terminal or command prompt.
3. Type the following command: `ssh -i /path/to/private/key user@hostname`.
   - Replace `/path/to/private/key` with the path to your private key file.
   - Replace `user` with your username on the remote host.
   - Replace `hostname` with the address or hostname of the remote host.
4. Press Enter, and if the key pair is valid, you will be connected to the remote host.

## The advantage of using #!/usr/bin/env bash instead of /bin/bash

Using `#!/usr/bin/env bash` as the shebang in a shell script has the advantage of being more portable. It allows the system to search for the `bash` executable in the user's `PATH`, ensuring that the script will work even if `bash` is installed in a different location.
