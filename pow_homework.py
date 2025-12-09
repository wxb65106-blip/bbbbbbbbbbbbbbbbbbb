import hashlib
import time

NAME = "bangbongo"

def mine(prefix_zero_count):
    target = "0" * prefix_zero_count
    nonce = 0

    start = time.time()

    while True:
        text = NAME + str(nonce)
        h = hashlib.sha256(text.encode()).hexdigest()

        if h.startswith(target):
            end = time.time()
            print("====== 难度", prefix_zero_count, "======")
            print("昵称:", NAME)
            print("找到的 nonce:", nonce)
            print("hash:", h)
            print("耗时:", end - start, "秒\n")
            return nonce, h

        nonce += 1

mine(4)
mine(5)
