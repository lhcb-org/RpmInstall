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

        reposdpath = installArea.yumreposd

        if not os.path.exists(reposdpath):
            os.makedirs(reposdpath)

        atlrepo = os.path.join(reposdpath, "atlas.repo")
        if not os.path.exists(atlrepo):
            yplf = open(atlrepo, 'w')
            yplf.write(installArea._getYumRepo("repo", "http://atlas-computing.web.cern.ch/atlas-computing/links/reposDirectory/lcg/slc6/yum/"))
            yplf.close()


    def getRelocateCommand(self, siteroot):
        """ Returns relocate command to be passed to RPM for the repositories """
        rpmcmd = " --relocate %s=%s " % ('/opt/lcg', os.path.join(siteroot, 'lcg', 'releases'))
        rpmcmd += " --relocate %s=%s " % ('/opt/atlas', siteroot)
        rpmcmd += " --badreloc "
        return rpmcmd
     


