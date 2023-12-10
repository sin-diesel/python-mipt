
import base64

message = input()
encoded = base64.urlsafe_b64encode(message.encode("UTF-8"))
print(encoded.decode("UTF-8"))