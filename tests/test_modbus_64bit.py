import unittest

from zabbix_get import zabbix_get

class Modbus64BitTestCase(unittest.TestCase):

    host = "172.16.238.2:5020"
    
    # INT64(Signed) NOT IMLEMENTED
    # Big Endian
    @unittest.skip("Implement first")
    def test_modbus_datatype_int64_64bit_be_0(self):
        key = "modbus_read["+self.host+",1,14,3,X]"
        self.assertEqual(zabbix_get(key),'-4629812106207628676')
    # Mid-Little Endian
    @unittest.skip("Implement first")
    def test_modbus_datatype_int64_64bit_mle_0(self):
        key = "modbus_read["+self.host+",1,22,3,X,0]"
        self.assertEqual(zabbix_get(key),'-4629812106207628676')

    # Little Endian
    @unittest.skip("Implement first")
    def test_modbus_datatype_int64_64bit_le_0(self):
        key = "modbus_read["+self.host+",1,18,3,X,3]"
        self.assertEqual(zabbix_get(key),'-4629812106207628676')

    # Mid-Big Endian
    @unittest.skip("Implement first")
    def test_modbus_datatype_int64_64bit_mbe_0(self):
        key = "modbus_read["+self.host+",1,26,3,X,2]"
        self.assertEqual(zabbix_get(key),'-4629812106207628676')

    #UNSIGNED INT64
    # Big Endian
    def test_modbus_datatype_uint64_64bit_be_0(self):
        key = "modbus_read["+self.host+",1,14,3,I]"
        self.assertEqual(zabbix_get(key),'13816931967501922940')
    # Mid-Little Endian
    def test_modbus_datatype_uint64_64bit_mle_0(self):
        key = "modbus_read["+self.host+",1,22,3,I,0]"
        self.assertEqual(zabbix_get(key),'13816931967501922940')

    # Little Endian
    def test_modbus_datatype_uint64_64bit_le_0(self):
        key = "modbus_read["+self.host+",1,18,3,I,3]"
        self.assertEqual(zabbix_get(key),'13816931967501922940')

    # Mid-Big Endian
    def test_modbus_datatype_uint64_64bit_mbe_0(self):
        key = "modbus_read["+self.host+",1,26,3,I,2]"
        self.assertEqual(zabbix_get(key),'13816931967501922940')

    
    # FLOAT64(double)
    # Big Endian
    def test_modbus_datatype_double_64bit_be_0(self):
        key = "modbus_read["+self.host+",1,14,3,d]"
        self.assertEqual(zabbix_get(key),'-0.123450')
    # Mid-Little Endian
    def test_modbus_datatype_double_64bit_mle_0(self):
        key = "modbus_read["+self.host+",1,22,3,d,0]"
        self.assertEqual(zabbix_get(key),'-0.123450')

    # Little Endian
    def test_modbus_datatype_double_64bit_le_0(self):
        key = "modbus_read["+self.host+",1,18,3,d,3]"
        self.assertEqual(zabbix_get(key),'-0.123450')

    # Mid-Big Endian
    def test_modbus_datatype_double_64bit_mbe_0(self):
        key = "modbus_read["+self.host+",1,26,3,d,2]"
        self.assertEqual(zabbix_get(key),'-0.123450')



if __name__ == '__main__':
    unittest.main(verbosity=2)