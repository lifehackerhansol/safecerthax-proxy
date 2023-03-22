from mitmproxy import tls

ignored_tls_hosts = [
    "zoogie.github.io",
    "ocsp.digicert.com",
    "ars.ifuser.jp",
    "ars.ifuser.jp:20080",
    "sec.ifilter.jp"
]


class TLSWhitelist:
    def tls_clienthello(self, data: tls.ClientHelloData):
        sni = data.client_hello.sni
        if sni and sni in ignored_tls_hosts:
            print(f"TLS hello - ignoring {sni}")
            data.ignore_connection = True


addons = [
    TLSWhitelist()
]
