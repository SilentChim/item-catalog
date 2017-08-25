items-catalog

Items catalog that acts as a feature request app, allowing devs to upload requested
client changes to a repository.

Open Terminal

Download and install the VM configuration

You will need to sign up for a google account and set up a client id and secret.

Visit: http://console.developers.google.com

Navigate to the directory you have it stored:
Download the database

Start the virtual machine

Type ‘vagrant up’ into the command line
Connect to the virtual machine

Type ‘vagrant ssh’ into the command line
Once connected, find the files for running the tests

Type ‘cd /vagrant’ to navigate to the directory containing the files, and type ‘ls’ to list the files in the vagrant directory.
Navigate to the items-catalog folder inside the vagrant directory: type ‘cd items-catalog’
Type ‘ls’ to list the files in the items-catalog directory

Setting up the enviornment:

Run 'python db_setup.py'
Run 'python application.py'
Open your web browser and visit http://localhost:5000
The applications main page will open and you will need to click on login and then use Google+ to login.
