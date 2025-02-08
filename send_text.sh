#!/bin/bash
set -e

# prerequisites:
#
# setup twilio account
# install twilio: `npm install -g twilio-cli`
# run `twilio login`

# usage: send_text.sh "my message"

twilio api core messages create \
  --from "+18333224289" \
  --to "+14048614660" \
  --body "$@"
