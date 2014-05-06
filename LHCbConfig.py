#!/usr/bin/env python
"""
LbInstall specific config for ATLAS

"""
import os

class Config:

    def __init__(self):
        self.CONFIG_VERSION=1
    
    def initYUM(self, installArea):
        """ Initialize the YUM config """
        repourl = "http://test-lbrpm.web.cern.ch/test-lbrpm"
        if installArea.repourl != None:
            repourl =  installArea.repourl
        
        reposdpath = installArea.yumreposd
        yumrepolhcb = os.path.join(reposdpath, "lhcb.repo")
        yumrepolcg = os.path.join(reposdpath, "lcg.repo")
        extrasurl = "/".join([repourl, "extras"])
        rpmsurl = "/".join([repourl, "rpm"])
        lhcbsurl = "/".join([repourl, "lhcb"])

        if not os.path.exists(yumrepolhcb):
            yplf = open(yumrepolhcb, 'w')
            yplf.write(installArea._getYumRepo("lhcbold", rpmsurl))
            yplf.write(installArea._getYumRepo("lhcb", lhcbsurl))
            yplf.close()

        if not os.path.exists(yumrepolcg):
            lcgsurl = "http://service-spi.web.cern.ch/service-spi/external/rpms/lcg"
            yplf = open(yumrepolcg, 'w')
            yplf.write(installArea._getYumRepo("lcg", lcgsurl))
            yplf.close()


    def getPrefixes(self):
        """ Returns the prefix in this case """
	if group == None or group == "lhcb":
	    return "/opt/LHCbSoft/lhcb"
        else:
            return "/opt/lcg"

