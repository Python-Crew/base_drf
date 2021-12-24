from payment.banks.bankfactories import BankFactory


def gateway_payment_request(request, order, bank_type=None):
    factory = BankFactory()
    bank = factory.create(bank_type)
    bank.set_request(request)
    bank._gateway_amount = order.price_amount
    bank._order = order
    bank.ready()
    data = {"gateway_url": bank.get_gateway_payment_url()}
    return data


def gateway_verify_payment_request(request, bank_type):
    factory = BankFactory()
    bank = factory.create(bank_type)
    data = request.query_params
    verify_data = {}
    for i in data:
        verify_data[i] = data.get(i)
    data = {"verify_result": bank.verify(verify_data)}
    return data
