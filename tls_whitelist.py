from mitmproxy import tls

ignored_tls_hosts = [
    "zoogie.github.io"
]


class TLSWhitelist:
    def tls_clienthello(self, data: tls.ClientHelloData):
        sni = data.client_hello.sni
        if sni and sni in ignored_tls_hosts:
            data.ignore_connection = True


addons = [
    TLSWhitelist()
]
