#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then echo "Everything okay"

else
	echo "Error! 127.0.0.0.1 is not in /etc/hosts"
fi
