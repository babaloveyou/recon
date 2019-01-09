# coding: utf-8
import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", help="domain to scan")
    args = parser.parse_args()
    domain = args.domain
    cmd = "curl https://certspotter.com/api/v0/certs\?domain\=example.com | jq '.[].dns_names[]' | sed 's/\"//g' | sed 's/\*\.//g' | uniq | dig +short -f - | uniq | nmap -T5 -Pn -sS -i - -p 80,443,21,22,8080,8081,8443 --open -n -oG -".format(
        domain)
    os.system(cmd)
