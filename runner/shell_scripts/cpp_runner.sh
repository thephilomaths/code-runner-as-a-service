#! /bin/bash

TIMELIMIT=$1
COMMAND=$2
OUTPUT_FILENAME=$3
CODE_FILENAME=$4 # This will be full file path
INPUT_FILENAME=$5 # This will be full file path

OUTPUT=$(timeout "$TIMELIMIT" "$COMMAND" -o "$OUTPUT_FILENAME" "$CODE_FILENAME" && ./"$OUTPUT_FILENAME" < "$INPUT_FILENAME" 2>&1)

EXIT_CODE=$?

if [ "$EXIT_CODE" -eq 0 ]; then
   echo "$OUTPUT"
elif [ "$EXIT_CODE" -eq 124 ]; then
  echo "Time Limit Exceeded"
else
   echo "Error: $OUTPUT"
fi

