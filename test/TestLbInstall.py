'''
Created on Aug 6, 2012

@author: Ben Couturier
'''
import os
import unittest
from LbInstall import InstallProjectClient, LbInstallClient, selectClient

TESTCONFIG="LHCbConfig"

class Test(unittest.TestCase):


    def testOptsBinary(self):
        parser = InstallProjectClient(TESTCONFIG).parser
        opts, args = parser.parse_args(["--binary=xbin"]) #@UnusedVariable
        self.assertEquals(opts.binary, "xbin")

    def testOptsBinaryShort(self):
        parser = InstallProjectClient(TESTCONFIG).parser
        opts, args = parser.parse_args(["-b"]) #@UnusedVariable
        self.assertTrue(opts.useCMTCONFIG)

    def testArgParsing(self):
        parser = InstallProjectClient(TESTCONFIG).parser
        opts, args = parser.parse_args(["-b", "-d", "x", "titi", "toto"]) #@UnusedVariable
        self.assertTrue(opts.useCMTCONFIG)

    def testLbInstallClientBadCmd(self):
        client = LbInstallClient(TESTCONFIG, ["lbinstallcmd", "rpm", "testrpm"], True)
        rc = client.main()
        self.assertEquals(rc, 1)

    def testLbInstallClientRpm(self):
        client = LbInstallClient(TESTCONFIG, ["rpm", "-ivh", "testrpm"], True)
        rc = client.main()
        self.assertEquals(rc, 0)
        self.assertEquals(client.runMethod, "rpm")
        self.assertEquals(client.runArgs[0][0], "-ivh")
        self.assertEquals(client.runArgs[0][1], "testrpm")

    def testLbInstallClientList(self):
        client = LbInstallClient(TESTCONFIG, ["list", "BRUNEL"], True)
        rc = client.main()
        self.assertEquals(rc, 0)
        self.assertEquals(client.runMethod, "listpackages")
        self.assertEquals(client.runArgs[0], [ "BRUNEL" ])

    def testLbInstallClientInstallRpm(self):
        client = LbInstallClient(TESTCONFIG, ["install", "BRUNEL"], True)
        rc = client.main()
        self.assertEquals(rc, 0)
        self.assertEquals(client.runMethod, "installRpm")
        self.assertEquals(client.runArgs[0], "BRUNEL")
        self.assertEquals(client.runArgs[1], None)


    def testInstallProjectClientBin(self):
        os.environ['CMTCONFIG'] = "MYCONFIG"
        client = InstallProjectClient(TESTCONFIG, ["-d", "-b", "BRUNEL"], True)
        rc = client.main()
        self.assertEquals(rc, 0)
        self.assertEquals(client.runMethod, "install")
        self.assertEquals(client.runArgs[0], "BRUNEL")
        self.assertEquals(client.runArgs[1], None)
        self.assertEquals(client.runArgs[2], "MYCONFIG")

    def testInstallProjectClientBadBin(self):
        if 'CMTCONFIG' in os.environ.keys():
            del os.environ['CMTCONFIG']
        client = InstallProjectClient(TESTCONFIG, ["-b", "BRUNEL"], True)
        rc = client.main()
        self.assertEquals(rc, 1)
        # Should fail as env var isn't set

    def testInstallProjectClientCmdlineBin(self):
        os.environ['CMTCONFIG'] = "MYCONFIG"
        client = InstallProjectClient(TESTCONFIG, ["--binary=TOTO", "BRUNEL"], True)
        rc = client.main()
        self.assertEquals(rc, 0)
        self.assertEquals(client.runMethod, "install")
        self.assertEquals(client.runArgs[0], "BRUNEL")
        self.assertEquals(client.runArgs[1], None)
        self.assertEquals(client.runArgs[2], "TOTO")

    def testInstallProjectClientFullLine(self):
        os.environ['CMTCONFIG'] = "MYCONFIG"
        client = InstallProjectClient(TESTCONFIG, ["--binary=TOTO", "BRUNEL", "vXrY"], True)
        rc = client.main()
        self.assertEquals(rc, 0)
        self.assertEquals(client.runMethod, "install")
        self.assertEquals(client.runArgs[0], "BRUNEL")
        self.assertEquals(client.runArgs[1], "vXrY")
        self.assertEquals(client.runArgs[2], "TOTO")

    def testInstallProjectClientNobin(self):
        os.environ['CMTCONFIG'] = "MYCONFIG"
        client = InstallProjectClient(TESTCONFIG, ["BRUNEL", "vXrY"], True)
        rc = client.main()
        self.assertEquals(rc, 0)
        self.assertEquals(client.runMethod, "install")
        self.assertEquals(client.runArgs[0], "BRUNEL")
        self.assertEquals(client.runArgs[1], "vXrY")
        self.assertEquals(client.runArgs[2], None)

    def testSelectClient1(self):
        args = [ "-d", "install", "toto"]
        c = selectClient(args)
        self.assertEquals(c, LbInstallClient)

    def testSelectClient2(self):
        args = [ "--root=foobar", "rpm", "toto"]
        c = selectClient(args)
        self.assertEquals(c, LbInstallClient)

    def testSelectClient3(self):
        args = [ "--root=foobar", "list", "toto"]
        c = selectClient(args)
        self.assertEquals(c, LbInstallClient)

    def testSelectClient4(self):
        args = [ "--root=foobar", "-d", "-b", "Brunel"]
        c = selectClient(args)
        self.assertEquals(c, InstallProjectClient)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testOptions']
    unittest.main()
