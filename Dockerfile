FROM archlinux:latest

RUN pacman-key --init \
    && pacman -Sy --noconfirm archlinux-keyring --needed \
    && pacman -Syu --noconfirm mitmproxy --needed \
    && ( yes | pacman -Scc ) && rm /var/lib/pacman/sync/*.db

RUN mkdir /mitm

WORKDIR /mitm

COPY start.sh .
COPY safecerthax.py .
COPY tls_whitelist.py .
COPY filter.py .

RUN chmod a+x start.sh

CMD ["/mitm/start.sh"]
