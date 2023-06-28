0x0C. Web server
- DevOps - SysAdmin

## How the Web Works
The World Wide Web functions through client-server communication. Clients, such as web browsers, send HTTP (Hypertext Transfer Protocol) requests to web servers. The servers process these requests and send back HTTP responses containing the requested data. Understanding this process is crucial for working with web servers effectively.

## Nginx
Nginx is a popular open-source web server and reverse proxy server known for its performance, scalability, and reliability. It can handle a large number of concurrent connections and efficiently serve static and dynamic content. Nginx is widely used in production environments and offers various features such as load balancing, caching, and SSL/TLS termination.

## Configuring Nginx
To configure Nginx, follow these steps:
1. Install Nginx on your system.
2. Locate the Nginx configuration files.
3. Understand the basic structure of the configuration files.
4. Modify the configuration based on your requirements, such as setting up server blocks, defining virtual hosts, and configuring proxy settings.
5. Test the configuration for syntax errors.
6. Restart or reload Nginx to apply the changes.

For detailed instructions and examples, refer to the Nginx documentation or relevant online resources.

## Child Process Concept
Web servers like Nginx use a concept called "child processes" to handle incoming requests. Child processes are spawned to manage concurrent connections efficiently. Each child process can handle multiple connections simultaneously, allowing the server to serve multiple clients concurrently without sacrificing performance or stability. Understanding the child process concept helps in optimizing server performance and managing system resources effectively.

## Root and Subdomains
In web server configuration, domains are divided into root domains and subdomains. A root domain represents the main domain, such as example.com, while subdomains are prefixes of the root domain, like subdomain.example.com. Nginx allows you to configure server blocks for handling different domains and subdomains. By properly configuring root and subdomains in Nginx, you can direct incoming requests to the appropriate server blocks and host multiple websites or applications on a single server.

## HTTP Requests
HTTP requests are the communication protocol between clients (such as web browsers) and web servers. They include methods like GET, POST, PUT, and DELETE, which define the actions to be performed by the server. Understanding the structure and handling of HTTP requests is essential for building and maintaining web applications. Web servers like Nginx process incoming HTTP requests and respond with the requested data or perform the specified actions.

## HTTP Redirection
HTTP redirection allows web servers to redirect clients from one URL to another. It is commonly used for URL rewriting, moving content to new locations, or handling specific conditions.
