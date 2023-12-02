#!/bin/bash

LINES=`cat input.txt`

# Part A
S=0
for LINE in $LINES:
do
	NUMBERS=$(echo $LINE | tr -dc '0-9')
	NUMBER="${NUMBERS: 0:1}${NUMBERS: -1}"
	S=$(($S+$NUMBER))
done

echo $S

# Part B
S=0
for LINE in $LINES:
do
  NUMBERS=""
  for (( i=0; i<${#LINE}; i++ ));
  do
    SUB_STR="${LINE:$i}" 
    if [[ $SUB_STR == [0-9]* ]]
    then
      NUMBERS="$NUMBERS""${SUB_STR: 0:1}"
    fi
    if [[ $SUB_STR == one* ]]
    then
      NUMBERS="$NUMBERS"1
    fi
    if [[ $SUB_STR == two* ]]
    then
      NUMBERS="$NUMBERS"2
    fi
    if [[ $SUB_STR == three* ]]
    then
      NUMBERS="$NUMBERS"3
    fi

   if [[ $SUB_STR == four* ]]
    then
      NUMBERS="$NUMBERS"4
    fi

   if [[ $SUB_STR == five* ]]
    then
      NUMBERS="$NUMBERS"5
    fi

   if [[ $SUB_STR == six* ]]
    then
      NUMBERS="$NUMBERS"6
    fi

   if [[ $SUB_STR == seven* ]]
    then
      NUMBERS="$NUMBERS"7
    fi
   if [[ $SUB_STR == eight* ]]
    then
      NUMBERS="$NUMBERS"8
    fi

  if [[ $SUB_STR == nine* ]]
    then
      NUMBERS="$NUMBERS"9
  fi
  done
  NUMBER="${NUMBERS: 0:1}${NUMBERS: -1}"
  S=$(($S+$NUMBER))
done
echo $S


