#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import socketserver
import http.server

RequestHandler = http.server.SimpleHTTPRequestHandler

PORT = 5000

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print("Server running on port", PORT)
    httpd.serve_forever()