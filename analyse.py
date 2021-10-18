import csv
import random
from tqdm import tqdm

transaction_dict = {}
identity_dict = {}
with open("train_transaction.csv", newline="") as f:
    spamreader = csv.reader(f)
    rows = 0
    for row in tqdm(spamreader):
        if rows == 0:
            rows = 1
        else:
            T_id = row[0]
            transaction_dict[T_id] = row[1:]

with open("train_identity.csv", newline="") as f:
    spamreader = csv.reader(f)
    rows = 0
    for row in tqdm(spamreader):
        if rows == 0:
            rows = 1
        else:
            T_id = row[0]
            identity_dict[T_id] = row[1:]

T_ids = transaction_dict.keys()
total = len(T_ids)

train_ids = random.sample(T_ids, 80000)
val_ids = list(set(T_ids).difference(set(train_ids)))
val_ids = random.sample(val_ids, 40000)
test_ids = random.sample(val_ids, 20000)
val_ids = list(set(val_ids).difference(set(test_ids)))

with open("mini_train_transaction.csv", 'w', newline='') as f:
    spamwriter = csv.writer(f)
    for id in train_ids:
        row = [id] + transaction_dict[id]
        spamwriter.writerow(row)

with open("mini_val_transaction.csv", 'w', newline='') as f:
    spamwriter = csv.writer(f)
    for id in val_ids:
        row = [id] + transaction_dict[id]
        spamwriter.writerow(row)

with open("mini_test_transaction.csv", 'w', newline='') as f:
    spamwriter = csv.writer(f)
    for id in test_ids:
        row = [id] + transaction_dict[id]
        spamwriter.writerow(row)

with open("mini_train_identity.csv", 'w', newline='') as f:
    spamwriter = csv.writer(f)
    for id in train_ids:
        if id in identity_dict:
            row = [id] + identity_dict[id]
            spamwriter.writerow(row)

with open("mini_val_identity.csv", 'w', newline='') as f:
    spamwriter = csv.writer(f)
    for id in val_ids:
        if id in identity_dict:
            row = [id] + identity_dict[id]
            spamwriter.writerow(row)

with open("mini_test_identity.csv", 'w', newline='') as f:
    spamwriter = csv.writer(f)
    for id in test_ids:
        if id in identity_dict:
            row = [id] + identity_dict[id]
            spamwriter.writerow(row)