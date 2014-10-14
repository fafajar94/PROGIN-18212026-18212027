#!/bin/sh

awk -F '<a href="' '{print $2}' satusatu.txt | awk -F '"' '{print $1}' > link.txt
