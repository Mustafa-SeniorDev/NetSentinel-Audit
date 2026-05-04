import asyncio
import socket

# NetSentinel-Audit: Advanced Network Security Scanner
# Author: Mustafa-SeniorDev (15+ Years Experience)

class PortScanner:
    def __init__(self, target):
        self.target = target

    async def check_port(self, port):
        """Asynchronously checks if a specific port is open."""
        conn = asyncio.open_connection(self.target, port)
        try:
            # Setting a timeout to show network efficiency handling
            reader, writer = await asyncio.wait_for(conn, timeout=1.0)
            print(f"[+] Port {port} is OPEN - Service detected.")
            writer.close()
            await writer.wait_closed()
            return port
        except:
            return None

    async def run_scan(self, port_range):
        """Orchestrates the scanning process across multiple ports."""
        print(f"[*] Starting security audit on: {self.target}")
        tasks = [self.check_port(port) for port in port_range]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    target_ip = "127.0.0.1" # Example target
    scanner = PortScanner(target_ip)
    
    # Common security ports to audit
    common_ports = [21, 22, 23, 25, 53, 80, 443, 3306, 8080]
    asyncio.run(scanner.run_scan(common_ports))
