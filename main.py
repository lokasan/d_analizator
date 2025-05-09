def main(service_name: str) -> str:
    return f'Name service: {service_name}'


def core(message: str, _type: int):
    return f'Msg: {message} Type: {_type}'


if __name__ == '__main__':
    msg = main('Linera Cards')
    print(msg)
