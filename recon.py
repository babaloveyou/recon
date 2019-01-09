# coding: utf-8
import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", help="domain to scan")
    args = parser.parse_args()
    domain = args.domain
    cmd = "curl https://certspotter.com/api/v0/certs\?domain\={} | jq '.[].dns_names[]' | sed 's/\"//g' | sed 's/\*\.//g' | uniq".format(
        domain)
    os.system(cmd)
