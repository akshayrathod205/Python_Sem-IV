def compare(l1, l2):
    for i in range(len(l1)):
        if l1[i] >= l2[i]:
            return False
    return True

def merge(l1, l2):
    l1.extend(l2)
    print(l1)

