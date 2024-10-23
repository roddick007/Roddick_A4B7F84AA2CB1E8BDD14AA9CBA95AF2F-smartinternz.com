<?php

function calculateAge($birthdate) {
    // Split the birthdate into year, month, and day
    list($birthYear, $birthMonth, $birthDay) = explode('-', $birthdate);

    // Get the current year, month, and day
    $currentYear = date('Y');  // Use 'Y' for a 4-digit year
    $currentMonth = date('m'); // Use 'm' for month (01-12)
    $currentDay = date('d');   // Use 'd' for day (01-31)

    // Calculate age by subtracting the birth year from the current year
    $age = $currentYear - $birthYear;

    // Check if the current date is before the birthday this year
    if ($currentMonth < $birthMonth || ($currentMonth == $birthMonth && $currentDay < $birthDay)) {
        $age--;  // Decrease age if birthday hasn't occurred yet this year
    }

    return $age;  // Return the calculated age
}

// Test the function
$birthdate = '2005-07-15';
echo "Current age is: " . calculateAge($birthdate) . "\n";

?>
