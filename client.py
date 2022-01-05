#
# Start client.py
#

import requests
import json
import sys


def main(server, number):
    url = "http://localhost:4000/jsonrpc"

    # Example echo method
    int_num = int(number)
    payload = {
        "method": "prime",
        "params": {"number": int_num},
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(url, json=payload).json()

    #print(json.dumps(response))
    print(number + " is " + ("prime" if response["result"] else "not prime"))

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
    
#
# End client.py
#