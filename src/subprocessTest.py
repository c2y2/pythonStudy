#!/usr/bin/env python
# encoding: utf-8

import subprocess


def doShell(command):
    pip=subprocess.Popen(str(command),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    pip.wait()
    stdout=pip.communicate()
    print "".join(stdout).decode("gbk").encode("utf8")

def main():
    try:
        doShell("nslookup www.baidu.com")
    except Exception, err:
            print err
if __name__ == '__main__':
    main()