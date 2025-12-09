from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# 你的昵称 + 你 POW 找到的 nonce
NAME = "bangbongo"
NONCE = "2533730"   # 把这里改成你自己的难度5的 nonce

message = (NAME + NONCE).encode()

# 生成 RSA 公私钥
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# 使用私钥签名
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("签名成功：")
print(signature.hex())

# 使用公钥验证签名
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("验证成功：签名有效！")
except:
    print("验证失败：签名无效")
