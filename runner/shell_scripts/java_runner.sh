TIMELIMIT=$1
COMMAND=$2
OUTPUT_FILENAME=$3
CODE_FILENAME=$4
INPUT_FILENAME=$5

OUTPUT=$("$COMMAND" "$CODE_FILENAME" && timeout "$TIMELIMIT" java "$OUTPUT_FILENAME" < "$INPUT_FILENAME" 2>&1)

EXIT_CODE = $?

if [ "$EXIT_CODE" -eq 0 ]; then
   echo "$OUTPUT"
elif [ "$EXIT_CODE" -eq 124 ]; then
  echo "Time Limit Exceeded"
else
   echo "Error: $OUTPUT"
fi
