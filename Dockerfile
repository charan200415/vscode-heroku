FROM docker pull ideasofcharan/kali:xrdp

RUN ./ngrok authtoken 25fucWxC3CSDqgaijavm6m1Zjtr_6eFf5H7wpMkwdHxaWXDwg

ENTRYPOINT ["/etc/init.d/xrdp status && /etc/init.d/xrdp restart && /etc/init.d/xrdp status && ./ngrok tcp 3390 "]
