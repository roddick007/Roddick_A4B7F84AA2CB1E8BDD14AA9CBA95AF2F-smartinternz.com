<?php
function calculate_age($birth_date) {
    // Split the birth date into year, month, and day
    list($birth_year, $birth_month, $birth_day) = explode('-', $birth_date);

    // Get the current date
    $current_year = date('Y');
    $current_month = date('m');
    $current_day = date('d');

    // Calculate age
    $age = $current_year - $birth_year;

    // Adjust age if the current month and day have not reached the birthday yet
    if ($current_month < $birth_month || ($current_month == $birth_month && $current_day < $birth_day)) {
        $age--;
    }

    return $age;
}

// Example usage
$birth_date = '1975-01-16';
echo "Current age is: " . calculate_age($birth_date);
?>
