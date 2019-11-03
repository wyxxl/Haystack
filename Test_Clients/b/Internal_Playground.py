from DynamicPublicLedger_Module import Dynamic_Public_Ledger
from Haystack_Module import Sender_Client
from Inbox_Module import Trusted_Paths
from IOTA_Module import *
from User_Modules import User_Profile

DLP_Accounts = [['JSXBGHSPAOFESHAVVBRUFHZYNSRBLRSYUOWYLNU9WOAJOJWA9MKIJIU9HUC9EREA9FNTL9NJJEK9EUKVC', '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwhEEPJBaCUTJl6ACRZGi\n0czLiaHVfHOQVrcA7WgUPqMtaSVnTTe6KQ0MCSTu525RCfWYPM8CcVWBbzaleXKg\nRis65tfQn1Atn6Womf7JpbGsUhymvsbCB+SVdNyXPBE0nBlyPzdOMzM6oXpA9r5d\n1vP8AuMjFRcwDB3Gc7UXBISKtFyFT3tF4f5ooOdWxzNP1hRiy4iTZvgkeNyOCko1\njbFkgUL0Og6gWbqc3T785OS7j4f4JvOiuDSFYrYjusuGWQcSlIVJRJTXYNsLDCA3\nCF9EJ4razUXuSW1+KOdWU4NOeBWLPtOyyFWsst1J1hkgjwB4ROeR/+AUUYw7Eaai\nywIDAQAB\n-----END PUBLIC KEY-----'], ['KPIDQXPYIVMESAPSXMXLAJFRKUJZFGOSBXZLDRGOMJCJTDDSWPVMNGHEBHQHN9AQV9KUTVSODKIVSVCNW', '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqjl0qGSjMAb0XFicS45h\nxVBCxvprisE2pKuOgrg/lKHx7zqf9V6f6W6tkmo0megeTnjuUOBYHssdknmNf4Cx\nVysWp2bWVArfMh9eJWlmJh68ASYQ/6aeGMMLgWWuHeG6RYskaNEybgPZPOKLutCh\nqI0v8AJslBADU8Jd45BPivuT3yDeJYPhKLvrJ5AsmcqvPh0i5A34rYSe2XLvYUT0\nBZq4anYc3z5BWgTyvXc1QIBXoIZlJ16MDCVaqiPu5yc/rkWKQk6pbr2Pv/mju4jH\nDuH5S/pDI8M2rdP2JGF0HPnQB91c0k+ieIaMaVi0xTYa48iGViDEGMHDPFpTNoVy\nwwIDAQAB\n-----END PUBLIC KEY-----'], ['MTWWXKPSZPDLSMKBFYKHUMJDJDRGJBCMBDMERHUWNLWMAAJNWIPHUEDJBBSUBKKF9A9NOZFEQVLVAIWKD', '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2I+9QxdyPSSqXuGtEClS\n85LtsuUoMFT7WyL5ek3WmyPDSTk1CIUk+AVrI3KOqQ3zdRM0iVzIy1iwBm4uKquL\nHrjPiNXjeQIH5PQF2QNDQVMJIKNm7DKzGOpwtkJSQRucwgoGCqIEHaqDfTgzCeXt\nOLwHryGylNAsOkWPgNQp4ERf0psuzv0Q4CPJ3bibS0YGMT/BrPmzWU5L5ZZgEpt0\n/AgEOZ8GCM3//ws2Ntq7TH0jnvt+XDsnHkdSvTkUZfPMc4Fbsmsg7sNZDS1fgwa4\n1oKCAQJuLbV43oXut8rzG9dCG+IMuWY7kazeK5fIeeggoY1iEZ6qaN5GNvGpI+V4\nCwIDAQAB\n-----END PUBLIC KEY-----'], ['LDXY9PWRYHGUKMVZVILJQXOYTGZCBJHJWVCQFRYOVVEJROLRTFWZDMCHXFCBEVYRVOYTRVRMFAZRFRGPA', '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAou+I7Y3NCwcRpL/LtpNH\n99ylbz0xInPKSrP5taATEYTO5PilYVYhuOYiubdcaeeXEr4TrDPNvS8e0pXZ6Mwe\n69LBVrQgEkXRoq7Bq6d2XaI/yorkDGGLkKhxAFhAVMZt4kSSHqgtwOiLLOZ45z35\nViKk37uXZKH729u0ELjxQhtoGaRzJsxcuC05FGQHn9UYa60PXNoa2cGSKHHM+NlE\n44B1NzL9RIIUbAPnZIvatrS1Wi6ZrEVhqw2LgmI5JOMBXwJc6hBa775tUJuYlHUF\nLiwBs7hnuXRIESJUqC71XZHKbgMz3iaTMqd/LXEooS9pH0aHNSr7GYMckEWxeAWI\nfwIDAQAB\n-----END PUBLIC KEY-----'], ['HQ9FTJXYEIDULIK9PBYIIYHWXMMYGXPR9PSGXYI9VPJAVMOAFUQ9HOYJSDTYNTCDOR9FLKRHCHHICOLYC', '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAx4bESkbUJm2L5cWLI5rd\nTThTRI5iMHsPkXxOcneUS+btzM0KCelmukkHUi5WPSfpOcIxHL+VUHZi83xgEQnm\nclANy/vn2B7BmnwNJAooE9aKQCM/TSBxt1QJFWRLa9041eEPnNdHz5z9qL5ye54v\nmDsbGEJ/EY42XqeXqDYBfUXJzL5uMLxXFj2sBWBXOhblWC2nHjrII2pYWLpZu9FK\nx9Ne0Q7mI8TviQbZTL9Tru42Sv3u7bMIABet7qUrM91OZouO6hWPcijjo/qDnKez\nTsXxjaMZ8pzXr9I2ibTrPE9IcZKPTcOuvhfaBRgjmmfLLoacV4pDQBDF9fecITY+\nIQIDAQAB\n-----END PUBLIC KEY-----']]

def Test_DPL():
	DLP = Dynamic_Public_Ledger()
	DLP.Start_Ledger()
	print(DLP.Check_User_In_Ledger().Ledger_Accounts)
	print("#####")
	print(DLP.Check_User_In_Ledger(Current_Ledger = True).Ledger_Accounts)

def Test_Sender(Message, DLP_Accounts):
    Sender_Client().Send_Message(Message = Message, ReceiverAddress = DLP_Accounts[0][0], PublicKey = DLP_Accounts[0][1], DifferentPaths = 1)

def Test_Paths():
    x = Trusted_Paths()
    x.Catch_Up()

def Test_Trajectory():
    x = Trusted_Paths()
    y = Sender_Client().Ping_Function()
    x.Scan_Paths()

def Play():
	for i in range(15):
		print(IOTA_Module(Seed = User_Profile().Private_Seed).Generate_Address(Index = Dynamic_Public_Ledger().Calculate_Block().Block+i))
		print(IOTA_Module(Seed = User_Profile().Private_Seed).Generate_Address(Index = Dynamic_Public_Ledger().Calculate_Block().Block-i))

if __name__ == "__main__":
    #Test_Paths()
    #Test_DPL()
    Test_Sender(Message = "Did you receive my latest messsage bra???? This is a secret conversion.", DLP_Accounts = DLP_Accounts)
    #Test_Trajectory()
	#Play()
