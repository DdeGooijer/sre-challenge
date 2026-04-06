## Changelog

### Python app

* Updated flask version from 3.0.1 to 3.1.3
* Changed database user retrieval from Fetch All to Fetch One and 
* Removed password storage from logging
* Added /health endpoint for Kubernetes Health probe 
* Changed hard coded secret key to ENV VAR

### VM Setup
* Added VM configuration to run Python app as systemd service on Fedora 43 server
* App config directly gets pulled from repository
* Added README for running Flask app on Vagrant
