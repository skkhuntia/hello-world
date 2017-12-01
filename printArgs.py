#!/usr/bin/python

import sys

def printArguments(namespace, node_ip, pod_name):
    print("Namespace: \t" + namespace)
    print("Node IP: \t" + node_ip)
    print("Pod Name: \t" + pod_name)
    
    if namespace=="csp-qa":
        return true
