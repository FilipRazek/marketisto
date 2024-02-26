def build_url(base, endpoint, params):
    url = base + endpoint + "?"
    for key, value in params.items():
        url += key + "=" + value + "&"
    return url
