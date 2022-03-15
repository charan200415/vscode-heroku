FROM ideasofcharan/kali:xrdp

RUN ./ngrok authtoken 25fucWxC3CSDqgaijavm6m1Zjtr_6eFf5H7wpMkwdHxaWXDwg

COPY deploy-container/entrypoint.sh /usr/bin/deploy-container-entrypoint.sh
ENTRYPOINT ["/usr/bin/deploy-container-entrypoint.sh"]
