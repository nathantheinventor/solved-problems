wget "https://www.udebug.com/UVa/$1" 2> /dev/null

if [ "$2" = "cpp" ]; then
    g++ -std=c++11 $3.cpp -o $3
fi

inputIds=$(cat $1 | grep 'data-id="[0-9]*".*' -o | grep '^data-id="[0-9]*"' -o | grep "[0-9]*" -o)
probId=$(cat $1 | grep 'name="problem_nid" value="[0-9]*"' -o | grep "[0-9]*" -o)
for id in $inputIds
do
    curl -d "input_nid=$id" "https://www.udebug.com/udebug-custom-get-selected-input-ajax" 2> /dev/null | python3 ~/Downloads/solved-problems/uva/uhunt.py > $id.in
    input=$(cat $id.in)
    curl -d "problem_nid=$probId&input_data=$input&op=Get Accepted Output&form_id=udebug_custom_problem_view_input_output_form" "https://www.udebug.com/UVa/$1" > test.html 2> /dev/null
    cat test.html | tr '\n' '\a' | grep 'name="output_data" cols="60" rows="5" class="form-textarea">[^<]*</' -o | grep ">.*<" -o | grep "[^<>]*" -o | tr '\a' '\n' >$id.exp > $id.1.exp
    
    cat "$id.1.exp" | recode html..ascii > $id.exp
    
    if [ "$(cat $id.exp)" = "" ]; then
        echo "No expected output for $id"
    else
        echo "---------------------------"
        echo "Diff $id"
        echo "---------------------------"
        if [ "$2" = "cpp" ]; then
            ./$3 < $id.in > $id.out
            diff $id.out $id.exp
        else
            python3 $2.py < $id.in > $id.out
            diff $id.out $id.exp
        fi
    fi

    
    rm $id.in $id.exp $id.1.exp $id.out test.html
done

rm $1