import http.client
import json
import threading
import queue
import os
from tkinter import *
from tkinter.ttk import *

#0x0cfd4d31d3e008551ef6d0a7d99861d732cb75c3

class B2G_Wallet():
    def __init__(self):
        self.GETH = Geth_Connector()
        self.GUI = guicore()
        self.Node = 'external'
        self.Show_Desktop()
        self.GUI.start()
    def Show_Desktop(self):
        self.GUI.ADD({'Action': 'title', 'Name': 'Fenster', 'Text': "Rafaels B2G Wallet - 0.1.1"})

        self.GUI.ADD({'Action': 'create', 'Name': 'Separator0', 'Typ': 'Separator'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Separator0', 'Ausrichtung': 'horizontal'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Separator0', 'Row': 0, 'Col': 0,'CSpan':3, 'Sticky': 'EW', 'PadY': 10,'PadX':5})

        self.GUI.ADD({'Action': 'create', 'Name': 'Label_Node', 'Typ': 'Label'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Label_Node', 'Text':'Node:'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Label_Node', 'Row': 1, 'Col':0})
        self.GUI.ADD({'Action': 'create', 'Name': 'Combobox_Node', 'Typ': 'Combobox'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Combobox_Node', 'Breite':15,'Values':['external','local']})
        self.GUI.ADD({'Action': 'insert', 'Name': 'Combobox_Node', 'Text': 'external'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Combobox_Node', 'Status':'readonly'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Combobox_Node', 'Row': 1, 'Col':1})

        self.GUI.ADD({'Action': 'create', 'Name': 'Button_Node', 'Typ': 'Button'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Button_Node', 'Text':'Set node','Func':self.set_Node})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Button_Node', 'Row': 1, 'Col':2,'PadX':5})

        self.GUI.ADD({'Action': 'create', 'Name': 'Separator1', 'Typ': 'Separator'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Separator1', 'Ausrichtung': 'horizontal'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Separator1', 'Row': 2, 'Col': 0,'CSpan':3, 'Sticky': 'EW', 'PadY': 10,'PadX':5})

        self.GUI.ADD({'Action': 'create', 'Name': 'Label_Adresse', 'Typ': 'Label'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Label_Adresse', 'Text':'Address:'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Label_Adresse', 'Row': 3, 'Col':0})
        self.GUI.ADD({'Action': 'create', 'Name': 'Entry_Adresse', 'Typ': 'Entry'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Entry_Adresse', 'Breite':50})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Entry_Adresse', 'Row': 3, 'Col':1})
        
        self.GUI.ADD({'Action': 'create', 'Name': 'Button_Aktualisieren', 'Typ': 'Button'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Button_Aktualisieren', 'Text':'Refresh','Func':self.Aktualisieren})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Button_Aktualisieren', 'Row': 3, 'Col':2,'PadX':5})

        self.GUI.ADD({'Action': 'create', 'Name': 'Separator2', 'Typ': 'Separator'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Separator2', 'Ausrichtung': 'horizontal'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Separator2', 'Row': 4, 'Col': 0,'CSpan':3, 'Sticky': 'EW', 'PadY': 10,'PadX':5})

        self.GUI.ADD({'Action': 'create', 'Name': 'Label_Von', 'Typ': 'Label'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Label_Von', 'Text':'From:'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Label_Von', 'Row': 5, 'Col':0})
        self.GUI.ADD({'Action': 'create', 'Name': 'Entry_Von', 'Typ': 'Entry'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Entry_Von', 'Breite':50})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Entry_Von', 'Row': 5, 'Col':1})
        
        self.GUI.ADD({'Action': 'create', 'Name': 'Label_An', 'Typ': 'Label'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Label_An', 'Text':'To:'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Label_An', 'Row': 6, 'Col':0})
        self.GUI.ADD({'Action': 'create', 'Name': 'Entry_An', 'Typ': 'Entry'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Entry_An', 'Breite':50})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Entry_An', 'Row': 6, 'Col':1})

        self.GUI.ADD({'Action': 'create', 'Name': 'Label_Betrag', 'Typ': 'Label'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Label_Betrag', 'Text':'Amount:'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Label_Betrag', 'Row': 7, 'Col':0})
        self.GUI.ADD({'Action': 'create', 'Name': 'Entry_Betrag', 'Typ': 'Entry'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Entry_Betrag', 'Breite':50})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Entry_Betrag', 'Row': 7, 'Col':1})

        self.GUI.ADD({'Action': 'create', 'Name': 'Label_Passwort', 'Typ': 'Label'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Label_Passwort', 'Text':'Password:'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Label_Passwort', 'Row': 8, 'Col':0})
        self.GUI.ADD({'Action': 'create', 'Name': 'Entry_Passwort', 'Typ': 'Entry'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Entry_Passwort', 'Breite':50,'Show':'*'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Entry_Passwort', 'Row': 8, 'Col':1})

        self.GUI.ADD({'Action': 'create', 'Name': 'Button_Senden', 'Typ': 'Button'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Button_Senden', 'Text':'Send','Func':self.Senden})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Button_Senden', 'Row': 5, 'Col':2,'PadX':5,'RSpan': 4})

        self.GUI.ADD({'Action': 'create', 'Name': 'Separator3', 'Typ': 'Separator'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Separator3', 'Ausrichtung': 'horizontal'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Separator3', 'Row': 9, 'Col': 0,'CSpan':3, 'Sticky': 'EW', 'PadY': 10,'PadX':5})

        self.GUI.ADD({'Action': 'create', 'Name': 'Label_PrivateKey', 'Typ': 'Label'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Label_PrivateKey', 'Text':'Private Key:'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Label_PrivateKey', 'Row': 10, 'Col':0})
        self.GUI.ADD({'Action': 'create', 'Name': 'Entry_PrivateKey', 'Typ': 'Entry'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Entry_PrivateKey', 'Breite':50,'Show':'*'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Entry_PrivateKey', 'Row': 10, 'Col':1})
        self.GUI.ADD({'Action': 'create', 'Name': 'Label_Passwort2', 'Typ': 'Label'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Label_Passwort2', 'Text':'Password:'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Label_Passwort2', 'Row': 11, 'Col':0})
        self.GUI.ADD({'Action': 'create', 'Name': 'Entry_Passwort2', 'Typ': 'Entry'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Entry_Passwort2', 'Breite':50,'Show':'*'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Entry_Passwort2', 'Row': 11, 'Col':1})

        self.GUI.ADD({'Action': 'create', 'Name': 'Button_Import', 'Typ': 'Button'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Button_Import', 'Text':'Import','Func':self.Importieren})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Button_Import', 'Row': 10, 'Col':2,'PadX':5,'RSpan':2})

        self.GUI.ADD({'Action': 'create', 'Name': 'Separator4', 'Typ': 'Separator'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Separator4', 'Ausrichtung': 'horizontal'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Separator4', 'Row': 12, 'Col': 0,'CSpan':3, 'Sticky': 'EW', 'PadY': 10,'PadX':5})

        self.GUI.ADD({'Action': 'create', 'Name': 'Label_Passwort3', 'Typ': 'Label'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Label_Passwort3', 'Text':'Password:'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Label_Passwort3', 'Row': 13, 'Col':0})
        self.GUI.ADD({'Action': 'create', 'Name': 'Entry_Passwort3', 'Typ': 'Entry'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Entry_Passwort3', 'Breite':50})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Entry_Passwort3', 'Row': 13, 'Col':1})

        self.GUI.ADD({'Action': 'create', 'Name': 'Button_New', 'Typ': 'Button'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Button_New', 'Text':'New Wallet','Func':self.Neu})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Button_New', 'Row': 13, 'Col':2,'PadX':5})

        self.GUI.ADD({'Action': 'create', 'Name': 'Separator5', 'Typ': 'Separator'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Separator5', 'Ausrichtung': 'horizontal'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Separator5', 'Row': 14, 'Col': 0,'CSpan':3, 'Sticky': 'EW', 'PadY': 10,'PadX':5})

        self.GUI.ADD({'Action': 'create', 'Name': 'TextBox', 'Typ': 'Text'})
        self.GUI.ADD({'Action': 'config', 'Name': 'TextBox', 'Hoehe': 10, 'Breite': 80})
        self.GUI.ADD({'Action': 'draw', 'Name': 'TextBox', 'Row': 15, 'Col': 0,'CSpan':3})

        self.GUI.ADD({'Action': 'create', 'Name': 'Separator6', 'Typ': 'Separator'})
        self.GUI.ADD({'Action': 'config', 'Name': 'Separator6', 'Ausrichtung': 'horizontal'})
        self.GUI.ADD({'Action': 'draw', 'Name': 'Separator6', 'Row': 16, 'Col': 0,'CSpan':3, 'Sticky': 'EW', 'PadY': 10,'PadX':5})

    def set_Node(self):
        self.Node = self.GUI.GET_W('Combobox_Node').get()
        self.GUI.ADD({'Action': 'insert', 'Name': 'TextBox','Index':'0.0', 'Text': 'Node changed to: %s \n' % self.Node})
        if self.Node == 'local':
            self.GUI.ADD({'Action': 'insert', 'Name': 'TextBox','Index':'0.0', 'Text': 'try starting local node \n'})
            t = threading.Thread(target=os.system,args=('bash -c "/mnt/c/B2G/bitcoiinGo --rpc --rpcapi personal,eth,admin"',))
            t.start()
            self.GETH = Geth_Connector('localhost')
        if self.Node == 'external':
            self.GETH = Geth_Connector()
        
    def Aktualisieren(self):
        adresse = self.GUI.GET_W('Entry_Adresse').get()
        kontostand = self.GETH.eth_getBalance(adresse)
        self.GUI.ADD({'Action': 'insert', 'Name': 'TextBox','Index':'0.0', 'Text': 'Account: %s >> Balance: %s \n' % (adresse,kontostand)})
        if self.Node == 'external':
            self.Transaktionen()
        
    def Senden(self):
        Von = self.GUI.GET_W('Entry_Von').get()
        An = self.GUI.GET_W('Entry_An').get()
        Betrag = float(self.GUI.GET_W('Entry_Betrag').get())
        PW = self.GUI.GET_W('Entry_Passwort').get()

        #unlock wallet
        x = self.GETH.eth_unlock(Von,PW)
        if 'error' in x:
            if x['error']['message'] == 'no key for given address or file':
                self.GUI.ADD({'Action': 'insert', 'Name': 'TextBox','Index':'0.0', 'Text': 'no private key for given address, please import private key first\n'})
                return
            elif x['error']['message'] == 'could not decrypt key with given passphrase':
                self.GUI.ADD({'Action': 'insert', 'Name': 'TextBox','Index':'0.0', 'Text': 'wrong password\n'})
                return
            self.GUI.ADD({'Action': 'insert', 'Name': 'TextBox','Index':'0.0', 'Text': 'error while unlocking wallet\n'})
            return
        #make transaction
        if x['result']:
            x = self.GETH.eth_send(Von,An,int(Betrag*10**18))
            print(x)
            if 'error' in x:
                if x['error']['message'] == 'insufficient funds for gas * price + value':
                    self.GUI.ADD({'Action': 'insert', 'Name': 'TextBox','Index':'0.0', 'Text': 'insufficient funds\n'})
            if 'result' in x:
                if x['result']:
                    self.GUI.ADD({'Action': 'insert', 'Name': 'TextBox','Index':'0.0', 'Text': 'transaction successfully send to network\nTX-Hash: %s\n' % x['result']})
                else:
                    self.GUI.ADD({'Action': 'insert', 'Name': 'TextBox','Index':'0.0', 'Text': 'error while making transaction\n'})
        #lock wallet
        x = self.GETH.eth_lock(Von)
        
    def Importieren(self):
        key = self.GUI.GET_W('Entry_PrivateKey').get()
        PW = self.GUI.GET_W('Entry_Passwort2').get()

        x = self.GETH.eth_importkey(key,PW)
        self.GUI.ADD({'Action': 'insert', 'Name': 'TextBox','Index':'0.0', 'Text': 'wallet import successful, address: %s\n' % x['result']})
        
    def Neu(self):
        PW = self.GUI.GET_W('Entry_Passwort3').get()

        x = self.GETH.eth_newkey(PW)
        self.GUI.ADD({'Action': 'insert', 'Name': 'TextBox','Index':'0.0', 'Text': 'New wallet created, address: %s\n' % x['result']})
        
    def Transaktionen(self):
        adresse = self.GUI.GET_W('Entry_Adresse').get()
        x = self.GETH.get_transactions(adresse,10)
        if x != []:
            for X in x:
                self.GUI.ADD({'Action': 'insert', 'Name': 'TextBox','Index':'0.0', 'Text': 'TX >> amount: %s block: %s\n      from: %s\n      to: %s\n' % (X['Amount'],X['Block'],X['From'],X['To'])})

class Geth_Connector():
    def __init__(self,Host='rafaeldelanekro.de',Port=8545):
        self.Host = Host
        self.Port = Port

    def connect(self,data):
        conn = http.client.HTTPConnection(host=self.Host,port=self.Port)
        data = data.replace("'",'"')
        conn.request("POST", "/" , data, {'content-type':'application/json'})
        response = conn.getresponse().read()
        conn.close()
        obj = response.decode('utf-8')
        #print(obj)
        obj = json.loads(obj)
        return obj
    def eth_newkey(self,pw):
        data = '{"jsonrpc":"2.0","method":"personal_newAccount","params":["%s"],"id":1}' % pw
        return self.connect(data)
    def eth_importkey(self,key,pw):
        data = '{"jsonrpc":"2.0","method":"personal_importRawKey","params":["%s", "%s"],"id":1}' % (key,pw)
        return self.connect(data)
    def eth_getBlockByNumber(self,Block):
        data = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["%s", true],"id":1}' % hex(Block)
        return self.connect(data)
    def eth_getBlockByHash(self,Block=''):
        data = '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params":["%s", true],"id":1}' % Block
        return self.connect(data)
    def eth_syncing(self):
        data = '{"jsonrpc":"2.0","method":"eth_syncing","id":1}'
        return self.connect(data)
    def eth_network(self):
        data = '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
        block1 = self.connect(data)['result']
        block2 = hex(int(block1,16) - 100)
        data = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["%s", true],"id":1}' % block1
        b1 = self.connect(data)['result']
        data = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["%s", true],"id":1}' % block2
        b2 = self.connect(data)['result']
        blocktime = round( (int(b1['timestamp'],16) - int(b2['timestamp'],16)) / 100 ,1)
        net_diff = round( (( int( b1['difficulty'] ,16) + int( b2['difficulty'] ,16 )) / 2) / (10**9) ,4)
        net_hash = round( net_diff / blocktime ,4)
        return (blocktime,net_diff,net_hash)
    def eth_getWork(self):
        data = '''{"jsonrpc":"2.0","method":"eth_getWork","params":[],"id":73}'''
        return self.connect(data)
    def eth_submitWork(self,Solution):
        data = '{"jsonrpc":"2.0","method":"eth_submitWork","params":%s,"id":73}' % Solution
        return self.connect(data)
    def eth_create_wallet(self):
        data = '{}'
        return self.connect(data)

    def eth_getBalance(self,Adress=''):
        data = '{"jsonrpc":"2.0","method":"eth_getBalance","params":["%s", "latest"],"id":1}' % Adress
        return round(int(self.connect(data)['result'],16) / 10**18,8)
    
    def get_transactions(self,Adress='',blocks=10):
        data = '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
        akt_block = int(self.connect(data)['result'],16)
        all_Transactions = []
        start = akt_block - blocks
        while akt_block >= start:
            b = hex(akt_block)
            data = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["%s", true],"id":1}' % b
            block = self.connect(data)['result']
            for X in block['transactions']:
                if X['to'] == Adress.lower() or X['from'] == Adress.lower():
                    t = {'From':X['from'],'To':X['to'],'Amount':int(X['value'],16)/10**18,'Block':int(block['number'],16)}
                    all_Transactions += [t]
                    #print(t)
            akt_block -= 1
        return all_Transactions
    def get_mined_blocks(self,start=0,Adress=''):
        data = '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
        akt_block = int(self.connect(data)['result'],16)
        all_Blocks = []
        while start <= akt_block:
            b = hex(start)
            data = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["%s", true],"id":1}' % b
            block = self.connect(data)['result']
            if Adress.lower() == block['miner']:
                all_Blocks += [{'number':int(block['number'],16),'timestamp':int(block['timestamp'],16),'Wert':5}]
            for u in block['uncles']:
                data = '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params":["%s", true],"id":1}' % u
                uncle = self.connect(data)['result']
                if Adress.lower() == uncle['miner']:
                    all_Blocks += [{'number':int(uncle['number'],16),'timestamp':int(uncle['timestamp'],16),'Wert':3.75}]
            start += 1
        return all_Blocks
    
    def eth_unlock(self,Adress,Password):
        params = [Adress, Password]
        data = json.dumps({"jsonrpc":"2.0","method":"personal_unlockAccount","params":params,"id":1})
        return self.connect(data)

    def eth_lock(self,Adress):
        params = [Adress]
        data = json.dumps({"jsonrpc":"2.0","method":"personal_lockAccount","params":params,"id":1})
        return self.connect(data)
    
    def eth_send(self,From,To,Value,Fee='0x2540be400'):
        params = [{'from':From,
                   'to':To,
                   'gas':hex(21000),
                   'gasPrice':Fee,
                   'value':hex(Value)}]
        data = json.dumps({"jsonrpc":"2.0","method":"eth_sendTransaction","params":params,"id":1})
        return self.connect(data)

class guicore():
    def __init__(self):
        self.Todolist = queue.Queue()
        self.Fenster = Tk()
        self.Style = Style()
        self.Widgetlist = [{'Name': 'Fenster', 'Widget': self.Fenster}]

    def start(self):
        self.Core()
        self.Fenster.mainloop()

    def ADD(self, Aufgabe):
        self.Todolist.put(Aufgabe)

    def GET_T(self):
        try:
            a = self.Todolist.get(True,0.1)
        except:
            a = {}
        return a

    def ADD_W(self, Widget):
        self.Widgetlist += [Widget]

    def GET_W(self, Name):
        for i in self.Widgetlist:
            if i['Name'] == Name or i['Widget'] == Name:
                return i['Widget']
        return None

    def DEL_W(self, Name):
        for i in range(0, len(self.Widgetlist)):
            if self.Widgetlist[i]['Name'] == Name or self.Widgetlist[i]['Widget'] == Name:
                self.Widgetlist = self.Widgetlist[0:i] + self.Widgetlist[i + 1:]
                break

    def DEL_F(self, i):
        widget = self.GET_W(i)
        for i in widget.grid_slaves():
            if repr(type(i)) == "<class 'tkinter.ttk.Frame'>":
                self.DEL_F(i)
            else:
                i.grid_forget()
                self.DEL_W(i)
        widget.grid_forget()
        self.DEL_W(widget)

    def Core(self):
        Aufgabe = self.GET_T()
        try:
            if 'Action' in Aufgabe:
                if Aufgabe['Action'] == 'title':
                    widget = self.GET_W(Aufgabe['Name'])
                    widget.title(Aufgabe['Text'])
                elif Aufgabe['Action'] == 'create':
                    if not 'Anker' in Aufgabe:
                        Aufgabe.update([('Anker', self.Fenster)])
                    if Aufgabe['Typ'] == 'PhotoImage':
                        c = Aufgabe['Typ'] + '()'
                    else:
                        c = Aufgabe['Typ'] + '(self.GET_W(Aufgabe["Anker"]))'
                    widget = eval(c)
                    self.ADD_W({'Name': Aufgabe['Name'], 'Widget': widget})
                elif Aufgabe['Action'] == 'draw':
                    widget = self.GET_W(Aufgabe['Name'])
                    c = ''
                    if 'Row' in Aufgabe:
                        c += 'row=' + repr(Aufgabe['Row']) + ','
                    if 'Col' in Aufgabe:
                        c += 'column=' + repr(Aufgabe['Col']) + ','
                    if 'CSpan' in Aufgabe:
                        c += 'columnspan=' + repr(Aufgabe['CSpan']) + ','
                    if 'RSpan' in Aufgabe:
                        c += 'rowspan=' + repr(Aufgabe['RSpan']) + ','
                    if 'PadX' in Aufgabe:
                        c += 'padx=' + repr(Aufgabe['PadX']) + ','
                    if 'PadY' in Aufgabe:
                        c += 'pady=' + repr(Aufgabe['PadY']) + ','
                    if 'IPadX' in Aufgabe:
                        c += 'ipadx=' + Aufgabe['IPadX'] + ','
                    if 'IPadY' in Aufgabe:
                        c += 'ipady=' + Aufgabe['IPadY'] + ','
                    if 'In' in Aufgabe:
                        anker = self.GET_W(Aufgabe['In'])  # lint:ok
                        c += 'in_= anker,'
                    if 'Sticky' in Aufgabe:
                        c += 'sticky=' + Aufgabe['Sticky'] + ','
                    c = 'widget.grid(' + c + ')'
                    eval(c)
                elif Aufgabe['Action'] == 'insert':
                    widget = self.GET_W(Aufgabe['Name'])
                    if repr(type(widget)) == "<class 'tkinter.ttk.Entry'>" or repr(type(widget)) == "<class 'tkinter.Text'>" or repr(type(widget)) == "<class 'tkinter.ttk.Combobox'>":
                        if not 'Index' in Aufgabe:
                            Aufgabe.update([('Index', 'end')])
                        widget.insert(Aufgabe['Index'], Aufgabe['Text'])
                    elif repr(type(widget)) == "<class 'tkinter.ttk.Treeview'>":
                        if not 'Root' in Aufgabe:
                            Aufgabe.update([('Root', '')])
                        if not 'Index' in Aufgabe:
                            Aufgabe.update([('Index', 'end')])
                        widget.insert(Aufgabe['Root'], Aufgabe['Index'], iid=Aufgabe['ID'],
                                      values=Aufgabe['Values'])
                    elif repr(type(widget)) == "<class 'tkinter.ttk.Notebook'>":
                        if not 'Notebook' in Aufgabe:
                            Aufgabe.update([('Notebook', Aufgabe['Name'])])
                        frame = self.GET_W(Aufgabe['Frame'])
                        widget = self.GET_W(Aufgabe['Notebook'])
                        if not 'Image' in Aufgabe:
                            if not 'Key' in Aufgabe:
                                widget.add(frame)
                            else:
                                widget.add(frame, text=Aufgabe['Key'])
                        else:
                            bild = self.GET_W(Aufgabe['Image'])
                            widget.add(frame, text=Aufgabe['Key'], image=bild, compound=Aufgabe['Sticky'])
                    elif repr(type(widget)) == "<class 'tkinter.Listbox'>":
                        if not 'Index' in Aufgabe:
                            Aufgabe.update([('Index', 'end')])
                        widget.insert(Aufgabe['Index'], Aufgabe['Item'])
                elif Aufgabe['Action'] == 'hide':
                    widget = self.GET_W(Aufgabe['Name'])
                    widget.tab(Aufgabe['Frame'], state='hidden')
                elif Aufgabe['Action'] == 'delete':
                    widget = self.GET_W(Aufgabe['Name'])
                    if repr(type(widget)) == "<class 'tkinter.ttk.Notebook'>":
                        if not 'Notebook' in Aufgabe:
                            Aufgabe.update([('Notebook', Aufgabe['Name'])])
                        frame = self.GET_W(Aufgabe['Frame'])
                        widget = self.GET_W(Aufgabe['Notebook'])
                        widget.forget(frame)
                    elif repr(type(widget)) == "<class 'tkinter.ttk.Entry'>" or repr(type(widget)) == "<class 'tkinter.Text'>":
                        widget = self.GET_W(Aufgabe['Name'])
                        if not 'Start' in Aufgabe:
                            Aufgabe.update([('Start', 0)])
                        if not 'Stop' in Aufgabe:
                            Aufgabe.update([('Stop', 'end')])
                        widget.delete(Aufgabe['Start'], Aufgabe['Stop'])
                elif Aufgabe['Action'] == 'var':
                    widget = self.GET_W(Aufgabe['Name'])
                    if repr(type(widget)) == "<class 'tkinter.ttk.Checkbutton'>":
                        if not 'Typ' in Aufgabe:
                            Aufgabe.update([('Typ', 'int')])
                        if Aufgabe['Typ'] == 'int':
                            v = IntVar()
                            if not 'Value' in Aufgabe:
                                Aufgabe.update([('Value', 0)])
                            v.set(Aufgabe['Value'])
                            widget.var = v
                            widget.config(variable=widget.var)
                    elif repr(type(widget)) == "<class 'tkinter.ttk.Combobox'>":
                        if not 'Typ' in Aufgabe:
                            Aufgabe.update([('Typ', 'str')])
                        if Aufgabe['Typ'] == 'str':
                            v = StringVar()
                            if not 'Value' in Aufgabe:
                                Aufgabe.update([('Value', '')])
                            v.set(Aufgabe['Value'])
                            widget.var = v
                            widget.config(textvariable=widget.var)
                elif Aufgabe['Action'] == 'setvar':
                    widget = self.GET_W(Aufgabe['Name'])
                    widget.var.set(Aufgabe['Value'])
                elif Aufgabe['Action'] == 'tag':
                    widget = self.GET_W(Aufgabe['Name'])
                    widget.item(Aufgabe['Row'],tag=Aufgabe['Tag'])
                elif Aufgabe['Action'] == 'settag':
                    widget = self.GET_W(Aufgabe['Name'])
                    widget.tag_configure(Aufgabe['Tag'],background=Aufgabe['Hintergrund'])
                elif Aufgabe['Action'] == 'treecol':
                    widget = self.GET_W(Aufgabe['Name'])
                    if not 'Width' in Aufgabe:
                        Aufgabe.update([('Width', 10)])
                    if not 'MinWidth' in Aufgabe:
                        Aufgabe.update([('MinWidth', Aufgabe['Width'])])
                    if not 'Sticky' in Aufgabe:
                        Aufgabe.update([('Sticky','center')])
                    widget.column(Aufgabe['Col'], width=Aufgabe['Width'], minwidth=Aufgabe['MinWidth'], anchor=Aufgabe['Sticky'])
                    if 'Head' in Aufgabe:
                        widget.heading(Aufgabe['Col'], text=Aufgabe['Head'])
                elif Aufgabe['Action'] == 'set':
                    widget = self.GET_W(Aufgabe['Name'])
                    if repr(type(widget)) == "<class 'tkinter.ttk.Treeview'>":
                        widget.set(Aufgabe['Row'], Aufgabe['Col'], Aufgabe['Value'])
                elif Aufgabe['Action'] == 'bind':
                    widget = self.GET_W(Aufgabe['Name'])
                    widget.bind(Aufgabe['Event'], Aufgabe['Func'])
                elif Aufgabe['Action'] == 'do':
                    Aufgabe['Func']()
                elif Aufgabe['Action'] == 'select':
                    widget = self.GET_W(Aufgabe['Name'])
                    if repr(type(widget)) == "<class 'tkinter.ttk.Notebook'>":
                        widget.select(Aufgabe['Tab'])
                    else:
                        widget.select_set(Aufgabe['Index'])
                elif Aufgabe['Action'] == 'undraw':
                    widget = self.GET_W(Aufgabe['Name'])
                    for i in widget.grid_slaves():
                        i.grid_forget()
                    widget.grid_forget()
                elif Aufgabe['Action'] == 'erase':
                    widget = self.GET_W(Aufgabe['Name'])
                    for i in widget.grid_slaves():
                        if repr(type(i)) == "<class 'tkinter.ttk.Frame'>":
                            self.DEL_F(i)
                        else:
                            i.grid_forget()
                            self.DEL_W(i)
                    if repr(type(widget)) == "<class 'tkinter.Toplevel'>":
                        widget.destroy()
                    else:
                        widget.grid_forget()
                    self.DEL_W(widget)
                elif Aufgabe['Action'] == 'paint':
                    widget = self.GET_W(Aufgabe['Name'])
                    if Aufgabe['Element'] == 'Linie':
                        if 'Farbe' in Aufgabe: Farbe = Aufgabe['Farbe']
                        else: Farbe = 'black'
                        if 'Breite' in Aufgabe: Breite = Aufgabe['Breite']
                        else: Breite = 1
                        widget.create_line(Aufgabe['Coord'][0],Aufgabe['Coord'][1],Aufgabe['Coord'][2],Aufgabe['Coord'][3],fill=Farbe,width=Breite)
                elif Aufgabe['Action'] == 'config':
                    widget = self.GET_W(Aufgabe['Name'])
                    if 'Text' in Aufgabe:
                        widget.config(text=Aufgabe['Text'])
                    if 'Hintergrund' in Aufgabe:
                        widget.config(bg=Aufgabe['Hintergrund'])
                    if 'Func' in Aufgabe:
                        widget.config(command=Aufgabe['Func'])
                    if 'Config' in Aufgabe:
                        eval('widget.config(' + Aufgabe['Config'] + ')')
                    if 'Cursor' in Aufgabe:
                        widget.config(coursor=Aufgabe['Coursor'])
                    if 'Column' in Aufgabe:
                        widget.config(columns=Aufgabe['Column'])
                    if 'Show' in Aufgabe:
                        widget.config(show=Aufgabe['Show'])
                    if 'Breite' in Aufgabe:
                        widget.config(width=Aufgabe['Breite'])
                    if 'Hoehe' in Aufgabe:
                        widget.config(height=Aufgabe['Hoehe'])
                    if 'DispColumn' in Aufgabe:
                        widget.config(displaycolumns=Aufgabe['DispColumn'])
                    if 'Export' in Aufgabe:
                        widget.config(exportselection=Aufgabe['Export'])
                    if 'Status' in Aufgabe:
                        widget.config(state=Aufgabe['Status'])
                    if 'Values' in Aufgabe:
                        widget.config(values=Aufgabe['Values'])
                    if 'Data' in Aufgabe:
                        widget.config(data=Aufgabe['Data'])
                    if 'Ausrichtung' in Aufgabe:
                        widget.config(orient=Aufgabe['Ausrichtung'])
                    if 'YScroll' in Aufgabe:
                        scrollbar = self.GET_W(Aufgabe['YScroll'])
                        widget.config(yscrollcommand=scrollbar.set)
                    if 'XScroll' in Aufgabe:
                        scrollbar = self.GET_W(Aufgabe['XScroll'])
                        widget.config(xscrollcommand=scrollbar.set)
                    if 'Scrollcommand' in Aufgabe:
                        box = self.GET_W(Aufgabe['Box'])
                        if Aufgabe['Scrollcommand'] == 'X': widget.config(command=box.xview)
                        else: widget.config(command=box.yview)
                    if 'Wrap' in Aufgabe:
                        if repr(type(widget)) == "<class 'tkinter.Label'>":
                            widget.config(wraplength=Aufgabe['Wrap'])
                        if repr(type(widget)) == "<class 'tkinter.Text'>":
                            widget.config(wrap=Aufgabe['Wrap'])
                    if 'Select' in Aufgabe:
                        widget.config(selectmode=Aufgabe['Select'])
                self.Fenster.after(0, self.Core)
            elif 'Styling' in Aufgabe:
                if Aufgabe['Styling'] == 'create':
                    self.Style.theme_create(Aufgabe['Name'], parent="default")
                elif Aufgabe['Styling'] == 'set':
                    self.Style.theme_settings(Aufgabe['Name'], Aufgabe['Settings'])
                elif Aufgabe['Styling'] == 'use':
                    self.Style.theme_use(themename=Aufgabe['Name'])
                self.Fenster.after(0, self.Core)
            else:
                self.Fenster.after(1, self.Core)
        except Exception as e:
            #print(e)
            self.Fenster.after(0, self.Core)


B2G_Wallet()
