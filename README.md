# EncryptQR

Node CLI is on the way. For now, enjoy the python part!
## Example
```python
from EncryptQR import EncryptQR
test = EncryptQR()
test.encrypt("sensitiveinfo.txt", "badpassword", "aes128")
test.decrypt("test.png", "badpassword", "aes128")
```
