# Client-server info collector
## Info
###>_ This app collects system info from all client
###>_ Server side sends config with configuration info
###>_ Server then starts to serve simple web-page powered by Flask
###>_ Client side receives config and then collects system info and sends it to server via POST request with interval from config
###>_ Server app inserts info received from POST request into sqlite4 database file 
## Launch
### Server
Run script/send_configs.sh to send config to all clients
`./send_configs.sh port timeout`
NOTE: port should be the same as for flask `app.py`

After that run server/app.py. Webpage will be available on port 5000 by default

### Client

Just run client/client.py 
`python3 client.py`
Script starts receiving config and then collects info and sends it to server
