# ee_client_auth_demo
Google Earth Engine App (App Engine) using the Python API and OAuth 2.0 Client ID authentication

### Usage

This is tested using a Debian Linux SO (Ubuntu, Mint, etc)

1. You need to have a whiteliste email account in Google Earth Engine (https://earthengine.google.com/)
2. You need to have running the Python API (https://developers.google.com/earth-engine/python_install)
3. You need to follow instructions in *Custom Applications* (https://developers.google.com/earth-engine/app_engine_intro). In Step 2, follow the *OAuth 2.0 Client ID* part.
4. Clone this repo:

`git clone https://github.com/fitoprincipe/ee_client_auth_demo`

5. Rename the json private key to: `privatekey.json` and paste it to the root folder of the app `../ee_client_auth_demo/privatekey.json`
6. Open a terminal in the same folder and run

`dev_appserver.py app.yaml`

7. Open an Internet browser and go to http://localhost:8000/