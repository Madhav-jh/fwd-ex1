from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>TCP/IP Protocol</title>
<style>
  body { font-family: Arial, sans-serif; background: #f0f4f8; margin: 0; padding: 30px; }
  h1 { text-align: center; font-size: 48px; color: #1a3c6e; }
  h2 { font-size: 30px; color: #1a3c6e; }
  p, li { font-size: 22px; line-height: 1.6; }
  table { width: 100%; border-collapse: collapse; font-size: 22px; background: white; }
  th { background: #1a3c6e; color: white; padding: 14px; }
  td { border: 1px solid #999; padding: 14px; }
</style>
</head>
<body>

<h1>TCP/IP Protocol Suite</h1>
<p>TCP/IP (Transmission Control Protocol / Internet Protocol) is the set of rules that lets computers communicate over the internet.</p>

<h2>The 4 Layers</h2>
<table>
  <tr><th>Layer</th><th>Protocols</th><th>Job</th></tr>
  <tr><td>Application</td><td>HTTP, HTTPS, FTP, SMTP, DNS</td><td>User-facing services</td></tr>
  <tr><td>Transport</td><td>TCP, UDP</td><td>End-to-end delivery, ports</td></tr>
  <tr><td>Internet</td><td>IP, ICMP, ARP</td><td>Addressing and routing</td></tr>
  <tr><td>Network Access</td><td>Ethernet, Wi-Fi</td><td>Physical transmission</td></tr>
</table>

<h2>TCP vs UDP</h2>
<ul>
  <li><b>TCP:</b> reliable, connection-based, ordered (web, email, file transfer)</li>
  <li><b>UDP:</b> fast, connectionless, no guarantee (video calls, gaming, DNS)</li>
</ul>

<h2>How It Works</h2>
<ol>
  <li>Data is split into packets.</li>
  <li>TCP numbers each packet.</li>
  <li>IP adds source and destination addresses.</li>
  <li>Packets travel across routers to the destination.</li>
  <li>TCP reassembles them in order.</li>
</ol>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()