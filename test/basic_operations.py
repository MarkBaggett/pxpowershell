import unittest
import pxpowershell


class TestBasicPowershell(unittest.TestCase):

    def test_exec(self):
        x = pxpowershell.PxPowershell()
        x.start_process()
        self.assertEqual(b'test', x.run("write-host 'test'").strip() )
        self.assertEqual(b'ConsoleHost', x.run("(get-host).name").strip() )
        x.run("$markwashere=5")
        self.assertEqual(b"10", x.run("$markwashere+5").strip() )  
        x.run("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nls\n\n")
        self.assertEqual(b'test', x.run("write-host 'test'").strip() )
        x.run("""
        
        
        """)
        self.assertEqual(b'test', x.run("write-host 'test'").strip() )
        x.stop_process()


    def test_script(self):
        x = pxpowershell.PxPowershell()
        x.start_process()
        script="""function Hello 
{
    write-host "hello"  
}

Hello


"""  
        x.run(script)
        self.assertEqual(b"hello", x.run("Hello").strip())
        x.stop_process()



if __name__ == "__main__":
    unittest.main()