#!/usr/bin/env python

"""
This runs a command on a remote host using SSH.
"""

import sys, time, pexpect,  traceback
import subprocess
import xml.dom.minidom as minidom

def sshcmd (user, password, host, port):
    """
    This runs a command on the remote Ruckus AP. This handles the case when you try to
    connect to a new host and ssh asks you if you want to accept the public key
    fingerprint and continue connecting.
    """
    if port != '':
        host = "-p "+ port + " " + host
        
    ssh_newkey = 'Are you sure you want to continue connecting'
    # Create a new spawn object.
    child = pexpect.spawn('ssh %s' % (host))
       
    i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'Please login:'])
    
    # timeout: print and quit
    if i == 0: # Timeout
        print 'ERROR!'
        print 'No SSH_newkey nor login received. Here is what SSH said:'
        print child.before, child.after
        return None
    # no ssh public key, accept
    if i == 1: # SSH does not have the public key. Just accept it.
        child.sendline ('yes')
        i = child.expect([pexpect.TIMEOUT, 'Please login:'])
        if i == 0: # Timeout
            print 'ERROR!'
            print 'No login after SSH_newkey. Here is what SSH said:'
            print child.before, child.after
            return None
        # send username
        child.sendline(user)
    # login:
    if i == 2: # login
        child.sendline (user)

    i = child.expect([pexpect.TIMEOUT, 'password :'])
    if i == 0: # Timeout
        print 'ERROR!'
        print 'No password after login. Here is what SSH said:'
        print child.before, child.after
        return None
    # send password
    child.sendline(password)

   
    i = child.expect([pexpect.TIMEOUT, 'rkscli:'])
    if i == 0: # Timeout    
        print 'ERROR! rkscli timeout'
        print 'No rkscli for get after password.. Here is what SSH said:'
        print child.before, child.after
        return None
        
    return child



def getonlineclients ():
    global uname, passwd, hname, port, ifname
    # excute
    child = sshcmd (uname, passwd, hname, port)
    
    
    if child == None:
        pass
    else:
        for j in range(0, 16):
            getcmd = 'get client-info wlan'
            getcmd = getcmd + str(j)
            # send cmd
            child.sendline(getcmd)
        
            i = child.expect([pexpect.TIMEOUT, 'OK'])
            if i == 0: # Timeout    
                print 'ERROR!'
                print 'Timeout after GETcmd. Here is what SSH said:'        
                print child.before, child.after
            else:
                #print 'WLAN',j
                print child.before
                
        child.sendcontrol('d')

    # wait for eof
    child.expect(pexpect.EOF)
    # print out
    #print 'Sucess : EOF  ',child.before

if __name__ == '__main__':
    
    #read configurations here
    dom = minidom.parse("/root/config.xml")
    for node in dom.getElementsByTagName("interface"):
        iftype = node.getAttribute("iftype")
        hname = node.getAttribute("host")
        ifname =node.getAttribute("ifname")
        
    for node in dom.getElementsByTagName("ssh"):
        uname = node.getAttribute("user")
        passwd =node.getAttribute("passwd")
        port = node.getAttribute("port")
        
    if iftype == 'remote':
        #try get state first, if failed, try set capture
        try:
            getonlineclients() # get state. if sucessful, exit
            
        # get state failed. either by raise() or by system "pexpect" timeout
        except Exception as e:
            print str(e)
            traceback.print_exc()

