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
        reposdpath = installArea.yumreposd
        yumrepolhcb = os.path.join(reposdpath, "lhcb.repo")
        yumrepolcg = os.path.join(reposdpath, "lcg.repo")
        extrasurl = "/".join([repourl, "extras"])
        rpmsurl = "/".join([repourl, "rpm"])
        lcgsurl = "/".join([repourl, "lcg"])
        lhcbsurl = "/".join([repourl, "lhcb"])

        if not os.path.exists(yumrepolhcb):
            yplf = open(yumrepolhcb, 'w')
            yplf.write(installArea._getYumRepo("lhcbold", rpmsurl))
            yplf.write(installArea._getYumRepo("lhcb", lhcbsurl))
            yplf.close()
        if not os.path.exists(yumrepolcg):
            yplf = open(yumrepolcg, 'w')
            yplf.write(installArea._getYumRepo("lcg", lcgsurl))
            yplf.close()


    def getPrefix(self):
        """ Returns the prefix in this case """
        return "/opt/lhcb"

