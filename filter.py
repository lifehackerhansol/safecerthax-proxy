import re

from mitmproxy.proxy import server_hooks

allowed_snis = [
    'nus.c.shop.nintendowifi.net',
    'ias.c.shop.nintendowifi.net',
    'cas.c.shop.nintendowifi.net',
    'ecs.c.shop.nintendowifi.net',
    'conntest.nintendowifi.net',
    'cbvc.cdn.nintendo.net',
    'nppl.c.app.nintendowifi.net',
    'nasc.nintendowifi.net',
    'zoogie.github.io',
    'ars.ifuser.jp',
    'ars.ifuser.jp:20080',
    'sec.ifilter.jp',
    'ocsp.digicert.com'
]

allowed_sni_cdn_nintendowifi = re.compile("(?i)((?:.+\\.)?)(?:cdn\\.nintendowifi\\.net)")


class Filter:
    def server_connect(self, data: server_hooks.ServerConnectionHookData) -> None:
        sni = data.server.sni
        if sni is None:
            sni = data.client.sni or data.server.address and data.server.address[0]

        if sni is None:
            return

        if sni not in allowed_snis and re.fullmatch(allowed_sni_cdn_nintendowifi, sni) is None:
            data.server.error = "Proxy not for normal use. Please reset your proxy settings."


addons = [
    Filter()
]
