# B2G-Wallet V0.1.1

There are two ways of using the wallet:
- with external public node
- with local node (more secure)

For external node usage, follow the installation steps 1,4,5 and 7 only. For local node all steps required and while testing there where some issues starting the local node, if that happens you can fall back to external node usage.

Installation (windows):

1. install Python 3.6 or later, can be found here: https://www.python.org/downloads/

2. activate the windows feature for using linux programs

2.1. open windows power shell as administrator

2.2. copy and insert the following code:

     Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
     
2.3. restart PC

3. install ubuntu for windows, can be found in the microsoft store
https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows

4. create a new folder in "C:\B2G\"

5. copy the content of this repository into the folder

6. double klick initialize.py to initialize the blockchain

7. from now on you can start the wallet by double klick wallet.py. This will start your local node and the wallet itself.

8. to close the wallet, you can close the black window, with the blockchain text, then everything will close.

9. for updating replace the wallet.py with the new one, later autoupdate will be available




Usage (windows):
- when starting wallet.py, external node is selected automatically
- if you want to run a local node, then select local at node selection and press "Set node"
- let the node syncronize the chain, at first start it could take 1-3 hours, you will see messages like "Imported new chain segment ...", when it is synced, once synced it will take seconds to sync the node again

>> Read Balance:
- input the address you want to know the balance into "Address" field, then click "Refresh"
- Balance will appear in the box at the bottom, and if found, the transactions from the last 10 Blocks are displayed

>> Import Old Wallet
- at the time only private keys supported, other methods will follow shortly, as a workaround you MAY use myetherwallet to get your private key out of a keystore file or mnemonic phrase: https://vintage.myetherwallet.com/#view-wallet-info ,but be careful and think about security and risks, which may occur
- local node only: make sure your node is fully synced
- put in your private key into "Private Key" field
- set a password for securing your wallet against attacks or misusage, password is shown to make sure you make a secure one, you will need this password for making transactions
- click "Import", this action may take some time

>> Create New Wallet
- type in a password in the "Password" field at the bottom and click "New Wallet"
- in the Outbox you will see your new address displayed
- the private key is stored in the node secured with your password
- more advanced options will follow

>> Send B2G
- type your sending address in "From"
- the destination address in "To"
- "Amount" is the amount in full B2G, some examples:
     - 100 B2G      = 100
     - 12,593 B2G   = 12.593
     - 0.5 B2G      = 0.5
- input your password, which you had choosen at import/creating the wallet
- click "Send"
- it will use a normal gas price and limit to make the transaction, most the time it will be done within the next 1-3 blocks


These are all basic functions and its not user friendly, i know, but it should work and i'm working on advanced versions. If you have questions you can contact me via telegram (Rafael de la Nekro).
