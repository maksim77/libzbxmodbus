import unittest

from zabbix_get import zabbix_get

class ModbusConnectionStringTestCase(unittest.TestCase):

    host = "172.16.238.2:5020"
    host_rtutcp = "172.16.238.2:5021"

    
    # test enc:// (rtu over tcp)
    def test_modbus_test_rtutcp(self):
        key = "modbus_read[enc://"+self.host_rtutcp+",1,0,3,uint16]"
        self.assertEqual(zabbix_get(key),'49807')
    # test tcp:// (plain tcp)
    def test_modbus_tcp(self):
        key = "modbus_read[tcp://"+self.host+",1,1,3,uint16]"
        self.assertEqual(zabbix_get(key),'49677')
   
    # test serial /dev/ttyS0
    @unittest.skip("implement this first")
    def test_modbus_serial(self):
        key = "modbus_read[/dev/ttyS0,1,1,3,uint16]"
        self.assertEqual(zabbix_get(key),'49677')



if __name__ == '__main__':
    unittest.main(verbosity=2)