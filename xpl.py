import hashlib
import re
import itertools
import string

salt = "it6z" # Change for your salt
pattern = re.compile(r"^0e\d+$")
charset = string.ascii_lowercase + string.digits  # upper and lower case letters with digits

# Testing pattern for 1 to 5 chars
for length in range(1, 6):
    for candidate_tuple in itertools.product(charset, repeat=length):
        candidate = ''.join(candidate_tuple)
        hash_result = hashlib.md5((salt + candidate).encode()).hexdigest()
        if pattern.match(hash_result):
            print("Found:", candidate, "=>", hash_result)
