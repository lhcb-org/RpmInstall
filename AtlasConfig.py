#!/usr/bin/env python
"""
LbInstall specific config for ATLAS

"""

class Config:

    def __init__(self):
        self.CONFIG_VERSION=1
    
    def initYUM(self, installArea):
        """ Initialize the YUM config """

        reposdpath = instaArea.yumreposd

        if not os.path.exists(reposdpath):
            os.makedirs(reposdpath)

        atlrepo = os.path.join(reposdpath, "atlas.repo")
        if not os.path.exists(atlrepo):
            yplf = open(atlrepo, 'w')
            yplf.write(installArea._getYumRepo("repo", "http://atlas-computing.web.cern.ch/atlas-computing/links/reposDirectory/lcg/slc6/yum/"))
            yplf.close()

    def getPrefix(self):
        """ Returns the prefix in this case """
        return "/opt/atlas"

