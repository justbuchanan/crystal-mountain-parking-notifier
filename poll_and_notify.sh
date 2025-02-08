#!/bin/bash
set -e

POLL_INTERVAL=60

# wait for parking availability
until python main.py --day 9 --month 2; do
    sleep $POLL_INTERVAL;
done;

# notify
./send_text.sh "CRYSTAL PARKING AVAILABLE - https://parking.crystalmountainresort.com/"
