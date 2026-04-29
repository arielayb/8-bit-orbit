# 8-bit-orbit
A simulator for satellites in 8-bit graphics.


NGINX setup:

To generate a self-signed Root CA and use it to issue a server certificate for Nginx, follow these sequential OpenSSL steps: 
1. Create a Root Certificate Authority (CA) 
You first need your own CA to sign the server certificate. 

    Generate CA Private Key: 
    openssl genrsa -out ca.key 2048
    
    Generate Self-Signed CA Certificate:
    openssl req -x509 -new -nodes -key ca.key -sha256 -days 3650 -out ca.crt
    (Note: For the "Common Name," use a name like "My Internal CA".) 

2. Generate the Server Certificate

    Generate Server Private Key: 
    openssl genrsa -out server.key 2048
    
    Create Certificate Signing Request (CSR):
    openssl req -new -key server.key -out server.csr
    
    (Note: For the "Common Name," use your server's domain name or IP address.)
    
    Sign the Server Certificate with your CA:
    openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 825 -sha256
    (Note: Modern browsers often require validity periods under 825 days and Subject Alternative Names (SAN).) 

3. Configure Nginx 
For Nginx to use these files, update your server block: 

    Locate your Nginx configuration (often in /etc/nginx/sites-available/).
    Add the following directives for nginx.conf config below:

    server {
        listen 443 ssl;
        server_name your_domain.com;

        ssl_certificate /path/to/server.crt;
        ssl_certificate_key /path/to/server.key;

        # Optional: If you want to verify client certificates using your CA
        # ssl_client_certificate /path/to/ca.crt;
        # ssl_verify_client on;
    }

    Use code with caution.
    Test and Reload: Run sudo nginx -t then sudo systemctl reload nginx. 
