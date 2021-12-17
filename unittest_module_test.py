def calculate(w, h):
    return round(w/h**2,2)      # 最後的2是只計算小數點後的第幾位

def cmToM(cm):
    return cm/100

if __name__ == '__main__':
    import unittest
    class BmiTestCase(unittest.TestCase):

        def test_calculate(self):
            result = calculate(65, 1.75)
            self.assertEqual(21.22, result)

        def test_cmToM(self):
            result = cmToM(175)
            self.assertEqual(1.75, result)
        
    tests = [
        BmiTestCase('test_calculate'),
        BmiTestCase('test_cmToM')
    ]
    suite = unittest.TestSuite()
    suite.addTests(tests)

    runner = unittest.TextTestRunner()
    runner.run(suite)