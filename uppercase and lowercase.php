<?php

function convertCase($input) {
    $output = '';  // Initialize an empty string for the output

    // Loop through each character in the input string
    for ($i = 0; $i < strlen($input); $i++) {
        $char = $input[$i];  // Get the current character

        // Check if the character is uppercase
        if (ctype_upper($char)) {
            // Convert to lowercase
            $output .= strtolower($char);
        } else {
            // Convert to uppercase
            $output .= strtoupper($char);
        }
    }

    return $output;  // Return the converted string
}

// Test the function
$inputString = "Hello WORLD!";
echo "Original string: $inputString\n";
echo "Converted string: " . convertCase($inputString) . "\n";

?>
