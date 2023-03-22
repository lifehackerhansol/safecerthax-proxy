#!/bin/bash

/usr/bin/mitmdump \
  -s /mitm/safecerthax.py \
  --certs c.shop.nintendowifi.net=/mitm-extra/star.c.shop.nintendowifi.net.pem \
  --certs cdn.nintendo.net=/mitm-extra/star.cdn.nintendo.net.pem \
  --set client_certs=/mitm-extra/ctr-common-1.pem \
  --ssl-insecure \
  --set relax_http_form_validation \
  --set certhax_payload=/mitm-extra/safecerthax.bin \
  --set arm9_payload=/mitm-extra/kernelhaxcode_3ds.bin \
  --set tls_version_client_min=TLS1 \
  --set block_global=false
