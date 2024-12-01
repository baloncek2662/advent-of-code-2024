# !/bin/bash

# Create a .cookie file in same directory as get_input.sh and copy the entire
# value of your "cookie" from the advent of code wepage before running the script

CURRENT_DIR="$(dirname "$(realpath "$0")")"
source $CURRENT_DIR"/".cookie

if [ $# -ne 1 ] ; then :
    echo "Usage: ./get_input.sh <day>"
    exit 1
fi

if [ -z "$COOKIE" ] ; then :
    echo "COOKIE is unset"
    exit 2
fi

OUTPUT_NUMBER=$1
if [ ${#OUTPUT_NUMBER} -eq 1 ] ; then
    OUTPUT_NUMBER="0$1"
fi

curl "https://adventofcode.com/2024/day/$1/input" \
  -H "authority: adventofcode.com" \
  -H "cache-control: max-age=0" \
  -H "sec-ch-ua: 'Google Chrome';v='95', 'Chromium';v='95', ';Not A Brand';v='99'" \
  -H "sec-ch-ua-mobile: ?0" \
  -H "sec-ch-ua-platform: 'Linux'" \
  -H "upgrade-insecure-requests: 1" \
  -H "user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36" \
  -H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" \
  -H "sec-fetch-site: same-origin" \
  -H "sec-fetch-mode: navigate" \
  -H "sec-fetch-user: ?1" \
  -H "sec-fetch-dest: document" \
  -H "accept-language: en-US,en;q=0.9" \
  -H "cookie: $COOKIE" \
  --compressed > $CURRENT_DIR"/"inputs/day_$OUTPUT_NUMBER.txt
