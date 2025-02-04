<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>login</title>
</head>
<body>
    <form method="POST">
        {% csrf_token %}
        <label for="name">Full Name</label>
        <input type="text" id="name" name="name" required placeholder="Enter your name"><br>
        <label for="email">email</label>
        <input type="email" id="email" name="email" required placeholder="Enter your email"><br>
        <input type="submit" value="submit">


    </form>
</body>
</html>