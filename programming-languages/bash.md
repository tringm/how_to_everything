## Tricks

### Arguments
1. Check number of arguments. Eg if not equal 1:
    ```bash
    if [ $# -ne 1 ]; then
        #command
    fi
    ```
### Array
1. Declaring Array
    ```bash
    declare -a datasets=("cran" "all")
    ```
1. Expand the array as a single word
    ```bash
    echo "${datasets[*]}"
    ```
1. Join the array by some separator
    ```bash
    echo $(IFS=$'|'; echo "${datasets[*]}")
    ```
1. Split the string by some separator
    ```bash
    SEPARATOR='-'
    IN="my-string"
    IFS=$SEPARATOR read -r -a IN_AS_LIST <<< "$IN"
    ```
1. Append new element to array
    ```bash
    declare -a datasets=("cran" "all")
    datasets+=( "new" ) # append directly
    newDatasets=("${datasets[@]}" "new")
    ```
1. Remove last element of array
    ```bash
    unset 'ARR[${#ARR[@]}-1]'
    ```
1. Array indexes all but last n elements:
    ```bash
    ${ARR[@]:0:${#ARR[@]}-$N}
    ```
1. Check if array contains
    ```bash
    allowedArgs=( "haha" "hehe" )

    arrayContains () {
        local e match="$1"
        shift
        for e; do
            [[ "$e" == "$match" ]] && return 0;
        done
        return 1
    }

    arrayContains "haha" "${allowedArgs[@]}"
    isIn="$?"

    if  [[ $isIn -eq 0 ]]; then
        echo "yes"
    else
        echo "no"
    fi
    ```
    ***Remember***:
     * ```${allowedArgs[@]}```
     * ```"$?"```
