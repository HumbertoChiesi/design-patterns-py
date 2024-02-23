from collections import defaultdict


_subscribers = defaultdict(list)


def subscribe(subsject: str, fn):
    _subscribers[subsject].append(fn)


def post_subject(subsject: str, data):
    if subsject not in _subscribers:
        return

    for f in _subscribers[subsject]:
        f(data)
