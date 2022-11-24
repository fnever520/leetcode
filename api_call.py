import json
import requests
import time

class API:
    def __init__(self):
        self.self.env_var["DASHBOARD_USR"] = None
        self.var_end["DASHBOARD_KEY"] = None

    def update_api(self):
        endpoint = "/".join([self.endpoint, "resource/"])
        headers = {"content-type": "application/json"}
        data = data
        ret_code_list = [200]

        resp = requests.post(
            endpoint,
            verify=False,
            data=json.dumps(data),
            headers=headers,
            auth=(self.env_var["DASHBOARD_USR"], self.env_var["DASHBOARD_KEY"])
        )

        ret_code = resp.status_code

        #Retry request
        retry_count = 0
        while retry_count < 3:
            if ret_code in range(400, 600):
                print(
                    "RESTapi: POST request to {} timeout, retry in 20s...".format(endpoint)
                )
                time.sleep(20)
                resp = requests.post(
                    endpoint,
                    verify=False,
                    data = json.dumps(data),
                    headers=headers,
                    auth=(self.env_var["DASHBOARD_USR"],
                          self.env_var["DASHBOARD_KEY"])
                )
                ret_code = resp.status_code
                retry_count += 1
            elif ret_code in ret_code_list:
                break
        if ret_code not in ret_code_list:
            print("RESTapi: Fail to post to {} status code {}".format(endpoint, ret_code))
