#!/bin/bash
set -e

POLL_INTERVAL=30

# wait for parking availability
until python main.py; do
    sleep $POLL_INTERVAL;
done;

# notify
./send_text.sh "CRYSTAL PARKING AVAILABLE\n https://parking.crystalmountainresort.com/"
