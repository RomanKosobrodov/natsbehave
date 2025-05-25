
def messages_equal(nats_msg, msg):
    return nats_msg.subject == msg.subject \
        and nats_msg.headers == msg.headers \
        and nats_msg.data == msg.data


def partially_equal(dict_a, dict_b):
    intersect = set(dict_a.keys()) & set(dict_b.keys())
    if len(intersect) == 0:
        return False
    for k in intersect:
        if dict_a[k] != dict_b[k]:
            return False
    return True



def messages_match(nats_msg, msg):
    return nats_msg.subject == msg.subject \
        and partially_equal(nats_msg.headers, msg.headers) \
        and partially_equal(nats_msg.data, msg.data)


Comparator = {"equal": messages_equal,
              "match": messages_match}
