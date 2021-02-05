#! /bin/bash

TIMELIMIT=$1
COMMAND=$2
CODE_FILENAME=$3
INPUT_FILENAME=$4

OUTPUT=$("$COMMAND" "$CODE_FILENAME" && cd runner/codes && timeout "$TIMELIMIT" java "Solution" < /code_runner/"$INPUT_FILENAME" 2>&1)
EXIT_CODE=$?

if [ "$EXIT_CODE" -eq 0 ]; then
   echo "$OUTPUT"
elif [ "$EXIT_CODE" -eq 124 ]; then
  echo "Time Limit Exceeded"
else
   echo "Error: $OUTPUT"
fi
