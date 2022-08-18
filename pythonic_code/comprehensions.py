from typing import Iterable, Set
import re

NAVER_REGEX = r"https:\/\/pay\.naver\.com\/payments\/detail\/(?P<invoice_number>\d{8}NP4\d{9})"
mock_object = [
    'https://pay.naver.com/payments/detail/20220722NP4325823353',
    'https://pay.naver.com/payments/detail/20220704NP4237695010',
    'https://pay.naver.com/payments/detail/20220624NP4189698364',
    'https://order.pay.naver.com/orderStatus/2021122838624950',
    'https://order.pay.naver.com/orderStatus/2021120638456561'
]


def collect_invoice_numbers_from_order_urls(orders: Iterable[str]) -> Set[str]:
    """
    Given several orders in the form
        order_id

    Collect the unique invoice numbers found on those order urls, and return them
    """
    collected_invoice_numbers = set()
    for order in orders:
        matched = re.match(NAVER_REGEX, order)
        if matched is not None:
            invoice_number = matched.groupdict()["invoice_number"]
            collected_invoice_numbers.add(invoice_number)

    return collected_invoice_numbers


def collect_invoice_numbers_from_order_urls2(orders: Iterable[str]) -> Set[str]:
    matched_invoice_numbers = filter(None, (re.match(NAVER_REGEX, order) for order in orders))
    return {m.groupdict()["invoice_number"] for m in matched_invoice_numbers}


def collect_invoice_numbers_from_order_urls3(orders: Iterable[str]) -> Set[str]:
    return {
        matched.groupdict()["invoice_number"]
        for order in orders
        if (matched := re.match(NAVER_REGEX, order)) is not None    # matched: temporary identifier
    }


print("============= first function: =============")
print(collect_invoice_numbers_from_order_urls(mock_object))
print("============= second function: =============")
print(collect_invoice_numbers_from_order_urls2(mock_object))
print("============= third function: =============")
print(collect_invoice_numbers_from_order_urls3(mock_object))
print("=============       end       =============")