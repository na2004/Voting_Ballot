#!/bin/bash

render_home() {
    echo "Content-Type: text/html"
    echo ""
    echo ""
    echo "<link rel='stylesheet' href='https://spar.isi.jhu.edu/teaching/443/main.css'>"
    echo "<h2 id='dlobeid-etovucca-voting-machine'>DLOBEID EtovUcca Voting Machine</h2>"
    echo "<h1 id='home'>Home</h1><br>"
    echo "<ul>"
    echo "<li><a href='./register.cgi'>Register to Vote</a></li>"
    echo "<li><a href='./vote.cgi'>Vote for an Office</a></li>"
    echo "<li><a href='./login.cgi'>Administrator Interface (Requires Login)</a></li>"
    echo "</ul>"
    echo "<h3>View Image</h3>"
    echo "<form method='get'>"
    echo "<label for='image'>Image Path:</label><br>"
    echo "<input type='text' id='image' name='image'><br>"
    echo "<input type='submit' value='View Image'>"
    echo "</form>"

    if [ ! -z "$QUERY_STRING" ]; then
        IFS='=&' read -r -a params <<< "$QUERY_STRING"
        for ((i=0; i<${#params[@]}; i+=2)); do
            if [ "${params[i]}" == "image" ]; then
                image_path="${params[i+1]}"
                echo "<h3>Image Content:</h3>"
                echo "<pre>"
                cat "$image_path" 2>/dev/null || echo "Error: Unable to read file"
                echo "</pre>"
            fi
        done
    fi
}

render_home
