import hashlib
import datetime
import random

class BigDataSecurityCompliance:
    def __init__(self):
        self.data_catalog = {}  # Data inventory and classification
        self.access_logs = []  # Audit logs
        self.encryption_keys = {} # Store encryption keys.
        self.data_breach_log = [] #Store data breach information.

    def add_data_source(self, source_name, data_type, sensitivity):
        """Adds a data source to the catalog."""
        self.data_catalog[source_name] = {"type": data_type, "sensitivity": sensitivity}

    def encrypt_data(self, data, key_name):
        """Encrypts data using a simple hashing algorithm (for demonstration)."""
        if key_name not in self.encryption_keys:
          self.encryption_keys[key_name] = str(random.randint(100000, 999999)) #generates a random key.

        key = self.encryption_keys[key_name]
        combined = f"{data}{key}".encode('utf-8')
        return hashlib.sha256(combined).hexdigest()

    def access_data(self, user, data_source):
        """Logs data access."""
        if data_source in self.data_catalog:
            self.access_logs.append({
                "timestamp": datetime.datetime.now(),
                "user": user,
                "data_source": data_source,
                "action": "access"
            })
            print(f"User {user} accessed {data_source}.")
        else:
            print(f"Data source {data_source} not found.")

    def data_breach(self, data_source, details):
        """logs a data breach"""
        self.data_breach_log.append({
            "timestamp": datetime.datetime.now(),
            "data_source": data_source,
            "details": details
        })
        print(f"Data breach detected in {data_source}. Details: {details}")

    def generate_audit_report(self):
        """Generates a simple audit report."""
        print("\nAudit Report:")
        for log in self.access_logs:
            print(f"  {log['timestamp']} - User: {log['user']}, Source: {log['data_source']}")

    def generate_breach_report(self):
        """Generates a simple breach report."""
        print("\nBreach Report:")
        for log in self.data_breach_log:
            print(f"  {log['timestamp']} - Source: {log['data_source']}, details: {log['details']}")

# Example Usage
security_system = BigDataSecurityCompliance()

security_system.add_data_source("customer_data", "PII", "restricted")
security_system.add_data_source("sales_data", "financial", "confidential")

encrypted_customer_data = security_system.encrypt_data("John Doe, 123 Main St", "customer_key")
print(f"Encrypted customer data: {encrypted_customer_data}")

security_system.access_data("admin", "customer_data")
security_system.access_data("analyst", "sales_data")

security_system.data_breach("customer_data", "Unauthorized access to customer records.")

security_system.generate_audit_report()
security_system.generate_breach_report()
