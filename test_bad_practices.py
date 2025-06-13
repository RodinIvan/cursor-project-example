import unittest
import os
import time
import random

# Bad import practices
from vulnerable_code import *
from config import *

class TerribleTestClass(unittest.TestCase):
    
    def setUp(self):
        # No proper setup
        pass
    
    def tearDown(self):
        # No cleanup
        pass
    
    def test_everything_in_one_test(self):
        """One massive test that tests everything (bad practice)"""
        # Testing multiple unrelated things
        handler = VulnerableDataHandler()
        
        # No assertions
        handler.execute_system_command("echo hello")
        handler.search_user("test")
        handler.weak_encryption("password")
        
        # Hardcoded values
        self.assertEqual(1 + 1, 2)
        self.assertTrue(True)
        
        # Testing with real system calls
        os.system("touch /tmp/test_file")
        
        # No cleanup of created files
        
    def test_with_sleep(self):
        """Test that wastes time"""
        time.sleep(5)  # Unnecessary delay
        self.assertTrue(True)
    
    def test_random_behavior(self):
        """Test with non-deterministic behavior"""
        random_value = random.randint(1, 100)
        # This test might randomly fail
        self.assertLess(random_value, 50)
    
    def test_no_assertions(self):
        """Test without any assertions"""
        x = 1 + 1
        y = 2 * 2
        # No assertions - test passes but doesn't verify anything
    
    def test_hardcoded_paths(self):
        """Test with hardcoded file paths"""
        # Hardcoded paths that won't work on all systems
        file_path = "/home/user/test_file.txt"
        # This will fail on Windows or different user accounts
        self.assertTrue(os.path.exists(file_path))
    
    def test_external_dependencies(self):
        """Test that depends on external services"""
        # Testing against real external service
        import urllib.request
        try:
            response = urllib.request.urlopen("https://httpbin.org/get")
            self.assertEqual(response.status, 200)
        except:
            # Silently ignoring network failures
            pass
    
    def test_database_without_mocking(self):
        """Test that uses real database"""
        # Using production database for testing
        handler = VulnerableDataHandler()
        # This could corrupt real data
        result = handler.search_user("test_user")
        # No verification of result
    
    def test_with_side_effects(self):
        """Test that modifies global state"""
        global API_KEY
        original_key = API_KEY
        API_KEY = "modified_key"
        # Not restoring original value
        self.assertEqual(API_KEY, "modified_key")
    
    def test_performance_without_limits(self):
        """Performance test without reasonable limits"""
        # This could run forever or consume all memory
        data = list(range(1000000))
        result = inefficient_processing(data)
        # No timeout or resource limits
    
    def test_security_with_real_commands(self):
        """Security test using real system commands"""
        handler = VulnerableDataHandler()
        # Actually executing dangerous commands in test
        result = handler.execute_system_command("whoami")
        # Could be dangerous if command is malicious

# Running tests without proper test runner
if __name__ == "__main__":
    # Poor test execution
    suite = unittest.TestLoader().loadTestsFromTestCase(TerribleTestClass)
    runner = unittest.TextTestRunner(verbosity=0)  # No verbose output
    runner.run(suite)
    
    # Additional bad practices
    print("All tests completed!")  # Using print instead of logging
    
    # Not checking test results
    # Not cleaning up test artifacts 