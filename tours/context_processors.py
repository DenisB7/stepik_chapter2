import data


def site_header(request):
    site_headers = {
        'title': data.title,
        'departure': data.departures,
    }

    return site_headers
