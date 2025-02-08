#!/bin/bash
set -e

# twilio login

# usage: send_text.sh "my message"

twilio api core messages create \
  --from "+18333224289" \
  --to "+14048614660" \
  --body "$@"
