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

    def getRelocateCommand(self, siteroot):
        """ Returns relocate command to be passed to RPM for the repositories """
        rpmcmd = " --relocate %s=%s " % ('/opt/lcg', os.path.join(siteroot, 'lcg', 'releases'))
        rpmcmd += " --relocate %s=%s " % ('/opt/LHCbSoft', siteroot)
        rpmcmd += " --badreloc "
        return rpmcmd

